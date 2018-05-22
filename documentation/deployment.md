## Deploying Fruitlist API ##

The file at `/documentation/fruitlist.Dockerfile` contains a template to create an image for the project.

When it is run, one should be able to enter `curl http://127.0.0.1:5000/showlist` and receive back a list of fruits.

To execute the project more manually on Windows with Python3 installed, one would need to:

> pip flask

> pip flask-httpauth

> SET FLASK_APP=app.py

> SET FLASK_ENV=production

> python -m flask run
