#!/usr/bin/python
from flask import Flask, jsonify

import socket

import datetime


app = Flask(__name__)


@app.route('/')

def api_home():

    hostname = socket.gethostname()

    ip = socket.gethostbyname(hostname)

    return jsonify({

            "hostname": hostname,

            "ip": ip,

            "timestamp": str(datetime.datetime.now()),

            "application": "Rango"
            "version": "VVVV"

        })


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=9355)
