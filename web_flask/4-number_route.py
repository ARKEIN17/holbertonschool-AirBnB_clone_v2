#!/usr/bin/python3
"""starts Flask application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """String to display"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """String to display in another route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """GET Route /c and <text> to print"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Print the text on the route"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/python', strict_slashes=False)
def python_is_default_cool(text='is cool'):
    """Print the text on the default route"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """Returns string if n is a number."""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )
