# day19_api_get
# GET request example using public PokeAPI

import requests

def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    resp = requests.get(url, timeout=10)
    if resp.status_code == 200:
        data = resp.json()
        # parse some useful fields
        types = [t["type"]["name"] for t in data["types"]]
        weight = data["weight"]
        abilities = [a["ability"]["name"] for a in data["abilities"]]
        print(f"Pokemon: {name}\nTypes: {types}\nWeight: {weight}\nAbilities: {abilities}")
    else:
        print(f"Failed to fetch {name}. Status: {resp.status_code}")

if __name__ == "__main__":
    get_pokemon("pikachu")
