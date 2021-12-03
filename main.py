from os import name
from flask import Flask, render_template, jsonify, make_response
import requests
import json
import random

app = Flask(__name__)

amount = 898
api = "https://pokeapi.co/api/v2"

@app.route("/<string:name>", methods=["POST", "GET"])
def get(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    req = requests.get(url)
    res = req.json()
    return jsonify(res)

@app.route("/")
def index():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    return render_template("pages/index.html", list=list)

if __name__ == "__main__":
    app.run(debug=True, port=5500)