#!/usr/bin/python3

"""
This module contains a flask app and an hbnb view that displays “HBNB”
when queried
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """View to print “Hello HBNB!” when root is queried"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """view called when /hbnb is queried"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """view called when /c/text is queried"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text="is cool"):
    """view called when /python is called with or without an argument"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    """view executed when the /number/<n> is queried"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    """view executed when the /number_template/<n> is queried"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """view executed when the /number_odd_or_even/<n> is queried"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
