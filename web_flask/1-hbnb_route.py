#!/usr/bin/python3
"""
1-hello_route module
"""

from flask import Flask

app = Flask(__name__)

"""
flask class idk
"""
@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"

"""
hbnb route
"""
@app.route("/hbnb", strict_slashes=False)
def hello_world():
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
