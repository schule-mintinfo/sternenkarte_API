#Dokumentation zur Sternenkarten API

####Funktionen
- API Status
- Aktueller Tag in Tag.Monat
- Neustart des PIs
- Herunterfahren des PIs
- Sternenkarte dreht sich auf bestimmten Tag stellen
- Sternenkarte zeigt ein bestimmtes Sternenbild
- Reset der Schrittmotoren 

####API Status
- url: 127.0.0.1:5000/
- return: {"Nachricht": "API online",  "color": "alert-primary"}

####Aktueller Tag
- url: 127.0.0.1:5000/date/today
- return: {"Nachricht": !Aktueller Tag!,  "color": "alert-primary"}

####Neustart des PIs
- url: 127.0.0.1:5000/reboot
- return: {"Nachricht": "System wird neu gestartet", "color": "alert-warning"}

####Herunterfahren des PIs
- url: 127.0.0.1:5000/shutdown
- return: {"Nachricht": "System fährt in 1min herunter", "color": "alert-danger"}

####Sternenkarte auf bestimmten Tag stellen
- url: 127.0.0.1:5000/date/!datum!
- Variablen: !datum! = Datum in Tag.Monat
- return: {"Nachricht": !Neigungswinkel!, "color": "alert-info"}

####Sternenkarte zeigt bestimmtes Sternenbild
- url: 127.0.0.1:5000/rotate/!ID!
- Variablen: !ID! = ID des Sternenbilds
- return: {"Nachricht": {"name": !Name!, "description": !Beschreibung!}, "color": "alert-info"}

####Reset der Schrittmotoren
- url: 127.0.0.1:5000/reset
- return: {"Nachricht": "Der Motor setzt sich auf null", "color": "alert-primary"}

###Vorgesehene Änderungen
- Schaltjahre werden in den Kalender integriert
- API Reboot
- Apache reload

