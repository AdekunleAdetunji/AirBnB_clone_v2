#!/usr/bin/python3

"""
This module contains a flask app and an hbnb view that displays “HBNB”
when queried
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """View to print “Hello HBNB!” when root is queried"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """view called when /hbnb is queried"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
