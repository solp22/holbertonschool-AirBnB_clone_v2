#!/usr/bin/python3
"""number route module"""

from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv


app = Flask(__name__)

"""routes"""


@app.route("/", strict_slashes=False)
def index():
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

"""number"""


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"

"""number template"""


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

"""odd or even template"""


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even_template(n):
    if n % 2 == 0:
        result = "is even"
    else:
        result = "is odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)


@app.teardown_appcontext
def close(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())


@app.route("/states/<id>", strict_slashes=False)
def states(state_id):
    return render_template('9-states.html',
                           states=storage.all(State).values(), id=state_id)


@app.route("/states", strict_slashes=False)
def states():
    return render_template('7-states_list.html',
                           states=storage.all(State).values())

"""host and port that the web app is listening"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
