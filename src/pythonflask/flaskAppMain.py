import argparse
import os
from flask import Flask
from flask import jsonify

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger('flaskAppMain')

from pythonflask.DataController import data_api
app = Flask(__name__)

app.register_blueprint(data_api)


@app.route("/hello")
def hello():
    return "Hello from flask!"

def init():
    log.info(__name__ + " initialized")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='port', help='Port for the flask server')

    args = parser.parse_args()

    if args.port:
        port = args.port
    else:
        port = 5000

    init()

    log.info("Starting flask server on port: {}".format(port))
    #app.run(host='0.0.0.0', port=port, debug=True)
    #app.run(debug=False)
    app.run(host='0.0.0.0', port=port)


