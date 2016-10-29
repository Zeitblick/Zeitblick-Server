Created during the culture hackathon [Coding Da Vinci Nord 2016](https://codingdavinci.de/) in Hamburg, Germany.    
[Info website (German)](https://hackdash.org/projects/57dd6cb2d9284f016c047471)

# Zeitblick Server

This is the backend for the "Zeitblick" app.  
It has been optimized for the "Google Cloud App Engine" (Standard Environment).

## Deployment ([Google App Engine](https://cloud.google.com/appengine/docs/python/))

1. **Dependencies:**
```
pip install -t lib -r requirements.txt
```
1. [MySQL Datenbank](https://cloud.google.com/sql/docs) (setup script will follow)
1. Rename the file `environment_template.py` into `environment.py` and adjust the information
