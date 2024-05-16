import requests

URL = "https://api.pokemonbattle.me/v2"
TOKEN = "fd60636d6c1c3001f9942da8efbc2a5c"
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Kai",
    "photo": "https://dolnikov.ru/pokemons/albums/017.png"
}

body_change = {
    "pokemon_id": "27594",
    "name": "Klaus",
    "photo": "https://dolnikov.ru/pokemons/albums/019.png"
}

body_pokeball = {
    "pokemon_id": "27594"
}

body_deletepokeball = {
    "pokemon_id": "27594"
}

body_knockout = {
    "pokemon_id": "27594"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER,  json = body_create)
print(response_create.text)

message = response_create.json()['message']

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)

response_deletepokeball = requests.put(url = f'{URL}/trainers/delete_pokeball', headers = HEADER, json = body_deletepokeball)
print(response_deletepokeball.text)

'''response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_knockout.text)'''

