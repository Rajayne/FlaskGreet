from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/<key>')
def variable(key):
    return f"Welcome {key}"