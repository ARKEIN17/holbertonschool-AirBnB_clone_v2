#!/usr/bin/python3
"""ini flask"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_route():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
