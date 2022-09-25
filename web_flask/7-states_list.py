#!/usr/bin/python3
"""FLASK MODULES"""


from models import *
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Return the list of the states rendered"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def storage_close(self):
    '''Close current session of sqlalchemy'''
    storage.close()


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )
