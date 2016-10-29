Entstanden im Rahmen des [Kulturhackathons Coding Da Vinci 2016](https://codingdavinci.de/).    
Zugehöriger [Hackdash Eintrag](https://hackdash.org/projects/57dd6cb2d9284f016c047471).

# Zeitblick Server / API

Dies ist das Backend für beide Zeitblick Apps.  
Es wurde für die "Google Cloud App Engine" (Standard Environment) angepasst.

## Deployment ([Google App Engine](https://cloud.google.com/appengine/docs/python/))

1. **Dependencies:**
```
pip install -t lib -r requirements.txt
```
1. [MySQL Datenbank](https://cloud.google.com/sql/docs) einrichten (mehr Infos und Setup-Skript folgen)
1. Die Datei `environment_template.py` in `environment.py` umbenennen und die Infos der MySQL Datenbank eintragen
