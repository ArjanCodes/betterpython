from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
