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
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>" + socket.gethostname() + " blah blah black" + os.uname()[1] + "<p>" + str(os.getpid()) + "</p>"

# app.run()