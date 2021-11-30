from os import name
from flask import Flask, render_template, jsonify, make_response
import requests
import json
import random

app = Flask(__name__)

amount = 898

@app.route("/<string:name>", methods=["POST", "GET"])
def get(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    req = requests.get(url)
    res = req.json()
    return jsonify(res)

@app.route("/generate", methods=["POST"])
def generate():
    name = random.randint(1, amount)
    return jsonify(name=name)

@app.route("/")
def index():
    name = random.randint(1, amount)
    return render_template("pages/index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True, port=5500)