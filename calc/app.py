# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/math/<function>')
def calc(function):
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = FUNCTIONS.get(function, "Not a valid function")
    if result == "Not a valid function":
        return result
    else:
        return f"{a} {function} by {b} equals {result(a,b)}"

FUNCTIONS = {
    'add': add,
    'subtract': sub,
    'multiply': mult,
    'divide': div
}