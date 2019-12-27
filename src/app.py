import flask
import os
import socket
import logging as logger

logger.basicConfig(level=logger.DEBUG)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    logger.debug(socket.gethostname())
    logger.debug('hello')
    return "<h1>Python Flask/Gunicorn testing/h1><p>Skeleton python application</p>" + socket.gethostname() + " blah blah black" + os.uname()[1] + "<p>" + str(os.getpid()) + "</p>"

# app.run()