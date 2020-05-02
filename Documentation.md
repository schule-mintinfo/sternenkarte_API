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

####Aktueller Tag
- url: 127.0.0.1:5000/date/today

####Neustart des PIs
- url: 127.0.0.1:5000/reboot

####Herunterfahren des PIs
- url: 127.0.0.1:5000/shutdown

####Sternenkarte auf bestimmten Tag stellen
- url: 127.0.0.1:5000/date/!datum!
- Variablen: !datum! = Datum in Tag.Monat

####Sternenkarte zeigt bestimmtes Sternenbild
- url: 127.0.0.1:5000/rotate/!ID!
- Variablen: !ID! = ID des Sternenbilds

####Reset der Schrittmotoren
- url: 127.0.0.1:5000/reset
