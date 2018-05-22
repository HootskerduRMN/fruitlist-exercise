# proposed dockerfile for fruitlist

FROM ubuntu:16.02
LABEL maintainer = "Joe Hootman <joe@hootman.org>"
LABEL description = "A web application using Flask to manage a list of fruits"
EXPOSE 5000 # flask-specific port
RUN sudo apt install python3-pip && \
	sudo pip3 install flask && \
	sudo pip3 install flask-httpauth && \
	mkdir fruitlist && \
	cd fruitlist/ && \
	git clone https://github.com/HootskerduRMN/fruitlist-exercise.git && \
	cd fruitlist-exercise/
ENV FLASK_APP=app.py
ENV FLASK_ENV=production # can change to "development" for debug
RUN sudo python3 -m flask run

# to test, use curl http://127.0.0.1:5000