import requests
import pytest

URL = "https://api.pokemonbattle.me/v2"
TOKEN = "fd60636d6c1c3001f9942da8efbc2a5c"
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2641'
TRAINER_NAME = 'Lagertha'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
     response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
     assert response_get.json()["data"][0]["trainer_id"] == '2641'
