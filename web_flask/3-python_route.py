#!/usr/bin/python3
"""python route module"""

from flask import Flask


app = Flask(__name__)

"""routes"""
@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"

"""hbnb"""
@app.route("/hbnb", strict_slashes=False)
def hello_world():
    return "HBNB"

"""c"""
@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    new = text.replace("_", " ")
    return f"C {new}"

"""python"""
@app.route("/python/", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    new = text.replace("_", " ")
    return f"Python {new}"

"""host and port that the web app is listening"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
