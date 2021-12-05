from logging import error
from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

api = "https://pokeapi.co/api/v2"

@app.route("/search/<string:name>", methods=["POST", "GET"])
def search(name):
    url = api + "/pokemon/" + name
    req = requests.get(url)
    res = req.json()
    return jsonify("", render_template("includes/card.html", res=res))

@app.route("/", methods=["POST", "GET"])
def index():
    pokemon = None
    name = None
    if request.method == "POST":
        name = request.form["name"]
        url = api + "/pokemon/" + name
        try:
            req = requests.get(url)
            res = req.json()
            pokemon = {}
            pokemon["name"] = res["name"]
            pokemon["id"] = "#" + str(res["id"])
            pokemon["type"] = res["types"][0]["type"]["name"]
            pokemon["height"] = res["height"]
            pokemon["weight"] = res["weight"]
            pokemon["sprite"] = res["sprites"]["other"]["dream_world"]["front_default"]
        except:
            pokemon = "Not Found"
    return render_template("pages/index.html", pokemon=pokemon, name=name)

if __name__ == "__main__":
    app.run(debug=True, port=5500) 