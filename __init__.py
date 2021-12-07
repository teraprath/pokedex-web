from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)
api = "https://pokeapi.co/api/v2"

@app.route("/", methods=["POST", "GET"])
def index():
    pokemon = None
    name = None
    if request.method == "POST":
        name = request.form["name"].lower().replace(" ", "-")
        url = api + "/pokemon/" + name
        try:
            req = requests.get(url)
            res = req.json()
            pokemon = {}
            pokemon["name"] = res["name"]
            
            pokemon["info"] = {}
            pokemon["info"]["id"] = "#" + str(res["id"])
            pokemon["info"]["exp"] = res["base_experience"]
            pokemon["info"]["height"] = str(res["height"]) + '"'
            pokemon["info"]["weight"] = str(res["weight"]) + "kg"

            pokemon["types"] = []
            n = len(res["types"])
            for i in range(n):
                type = res["types"][i]["type"]["name"]
                pokemon["types"].append(type)

            pokemon["stats"] = {}
            n = len(res["stats"])
            for i in range(n):
                j = res["stats"][i]["stat"]["name"]
                pokemon["stats"][j] = res["stats"][i]["base_stat"]

            pokemon["sprite"] = res["sprites"]["other"]["dream_world"]["front_default"]
            if pokemon["sprite"] == None:
                pokemon["sprite"] = res["sprites"]["front_default"]
        except:
            pokemon = "Not Found"
    return render_template("pages/index.html", pokemon=pokemon, req=name)

if __name__ == "__main__":
    app.run(debug=True, port=5500)
