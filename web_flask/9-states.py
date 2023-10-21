#!/usr/bin/python3
"""
This module contains views for a flask app
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def state(id=None):
    """
    view executed when the /state is queried with optional id parameter
    """
    if id:
        state = storage.all(State).get(f"State.{id}")
        return render_template("9-states.html", state=state, states=None)
    else:
        states = storage.all(State).values()
        return render_template("9-states.html", states=states, state=None)


@app.teardown_appcontext
def teardown(exception):
    """
    close connection to the storage after succesful retrieval from the database
    """
    storage.close()


app.run(host="0.0.0.0", port=5000)
