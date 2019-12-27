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
    logger.debug(os.getpid())
    return "<h1>Python Flask/Gunicorn testing</h1><p>Skeleton python application</p> Hostname - " + socket.gethostname() + " <br/> Hostname - " + os.uname()[1] + "<p> ProcessId - " + str(os.getpid()) + "</p>"

# app.run()