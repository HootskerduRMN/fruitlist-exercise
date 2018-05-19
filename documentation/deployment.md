## Deploying Fruitlist API ##

Deploy the project to a directory on a computer with a Python 3 interpreter installed (and the `python.exe` and `pip` commands in `PATH`):

1. From a terminal run `pip install bottle` and then `pip install bottle-cork`.
2. Run `python main.py`.

You then should be able to open a web browser and navigate to `http://127.0.0.1/showlist`

pip flask
pip flask-httpauth

have to SET FLASK_APP=main.py
or SET on unix export FLASK_APP=main.py

then to execute:
Windows (in project dir): python -m flask run
UNIX: flask run

