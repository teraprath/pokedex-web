import requests

api = "https://pokeapi.co/api/v2"

def getData(pokemon: str):
    name = pokemon
    url = api + "/pokemon/" + name
    pokemon = {}
    try:
        req = requests.get(url)
        res = req.json()
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

        del pokemon["stats"]["special-attack"]
        del pokemon["stats"]["special-defense"]

        pokemon["icons"] = []
        pokemon["icons"].append("HP")
        pokemon["icons"].append("AT")
        pokemon["icons"].append("DF")
        pokemon["icons"].append("SP")

        pokemon["ability"] = res["abilities"][0]["ability"]["name"]
        pokemon["sprite"] = res["sprites"]["other"]["dream_world"]["front_default"]
        if pokemon["sprite"] == None:
            pokemon["sprite"] = res["sprites"]["front_default"]
    except:
        pokemon = "Not Found"
    return pokemon