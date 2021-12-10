from flask import Flask, render_template, request
from requests.api import get
import pokeapi

app = Flask(__name__)

@app.route("/stats/<string:pokemon>")
def stats(pokemon):
    name = pokemon.lower()
    pokemon = pokeapi.getData(name)
    return render_template("pages/stats.html",  pokemon=pokemon)

@app.route("/", methods=["POST", "GET"])
def index():
    pokemon = None
    name = None
    if request.method == "POST":
        name = request.form["name"].lower().replace(" ", "-")
    else:
        name = request.args.get("name")

    if name != None:
        pokemon = pokeapi.getData(name)
        
    return render_template("pages/index.html", pokemon=pokemon, req=name)

@app.route("/niko")
def niko():
    return "Hurensohn"

if __name__ == "__main__":
    app.run(debug=True, port=5500)
