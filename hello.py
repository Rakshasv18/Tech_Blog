# hello.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login")
def hello_world():
    data = request.json
    return jsonify(data)
