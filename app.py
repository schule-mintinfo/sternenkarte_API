from flask import Flask, jsonify
import datetime
from subprocess import Popen as pop
import json
import serial

ser = serial.Serial('COM5', baudrate=9600, timeout=1)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"Nachricht": "API online",  "color": "alert-primary"})

@app.route('/date/today')
def heute():
    now = datetime.datetime.now()
    return jsonify({"Nachricht": str(now.strftime("%d. %m")),  "color": "alert-primary"})

@app.route('/reboot')
def reboot():
    pop("sudo reboot", shell=False)
    return jsonify({"Nachricht": "System wird neu gestartet", "color": "alert-warning"})

@app.route('/shutdown')
def shutdown():
    pop("sudo shutdown", shell=False)
    return jsonify({"Nachricht": "System fährt in 1min herunter", "color": "alert-danger"})


@app.route('/date/<string:data>')
def date(data):
    raw = str(data).rsplit("-")
    tag = raw[2]
    monat = raw[1]
    with open("MonatsConvert.json", "r", encoding='utf-8') as file1:
        data = json.load(file1)
        Tage = data[monat] + int(tag)
        with open("Daten.json", "r", encoding='utf-8') as file2:
            data = json.load(file2)
            degree = data[str(Tage)]
            cmd = "!" + str(degree)
            ser.write(cmd.encode(encoding='utf-8'))
    return jsonify({"Nachricht": str(degree), "color": "alert-info"})


@app.route('/rotate/<string:ID>')
def ID_User(ID):
    with open("IDs.json", "r") as file3:
        data = json.load(file3)
        steps = data[ID]['step_value']
        LEDindex = data[ID]['LEDindex']
        cmd = "#" + str(steps)
        ser.write(cmd.encode(encoding='utf-8'))
        cmd = "-" + str(LEDindex)
        ser.write(cmd.encode(encoding='utf-8'))
        ser.write("start".encode(encoding='utf-8'))
    return jsonify({"Nachricht": {"name": data[ID]['name'], "description": data[ID]['description']}, "color": "alert-info"})

@app.route('/reset')
def set0():
    ser.write("setZero")
    return jsonify({"Nachricht": "Der Motor setzt sich auf null", "color": "alert-primary"})


if __name__ == "__main__":
    app.run()

