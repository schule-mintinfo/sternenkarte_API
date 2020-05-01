from flask import Flask, jsonify
import datetime
import os
import json
import serial

ser = serial.Serial('', baudrate=9600, timeout=1)
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
    os.system("sudo reboot")
    return jsonify({"Nachricht": "System wird neu gestartet", "color": "alert-warning"})

@app.route('/shutdown')
def shutdown():
    os.system("sudo shutdown")
    return jsonify({"Nachricht": "System fährt in 1min herunter", "color": "alert-danger"})



@app.route('/date/<string:data>')
def date(data):
    raw = str(data).rsplit(".")
    tag = raw[0]
    monat = raw[1]
    with open("MonatsConvert.json", "r") as file1:
        data = json.load(file1)
        Tage = data[monat] + int(tag)
        with open("Daten.json") as file2:
            data = json.load(file2)
            degree = data[str(Tage)]
            ser.write("!" + str(degree))
    return jsonify({"Nachricht": str(degree), "color": "alert-info"})


@app.route('/rotate/<string:ID>')
def ID_User(ID):
    with open("IDs.json", "r") as file3:
        data = json.load(file3)
        steps = data[ID]['step_value']
        LEDindex = data[ID]['LEDindex']
        ser.write("#" + str(steps))
        ser.write("-" + str(LEDindex))
        ser.write("start")
    return jsonify({"Nachricht": {"name": data[ID]['name'], "description": data[ID]['description']}, "color": "alert-info"})

@app.route('/reset')
def set0():
    ser.write("setZero")
    return jsonify({"Nachricht": "Der Motor setzt sich auf null", "color": "alert-primary"})


if __name__ == "__main__":
    app.run()

