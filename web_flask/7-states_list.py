#!/usr/bin/python3
"""
This module contains an app that helps to view all state in my database
storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close(exception=None):
    """method to close connection to the database"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """view executed when the /states_list is queried"""
    states = storage.all(State)
    return render_template("7-states_list.html",
                           states=states)


app.run(host="0.0.0.0", port=5000)
