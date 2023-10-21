#!/usr/bin/python3

"""
Module to configure a flask web app to display “Hello HBNB!” when
root is queried
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """View to print “Hello HBNB!” when root is queried"""
    return "Hello HBNB!"


app.run(host="0.0.0.0", port=5000)
