import requests
import pytest 

host = 'https://api.pokemonbattle.me:9104'
token = '013ed52b598d866b2e96dda329f68959'


def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 1762})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': 1762})
    assert response.json()['trainer_name'] == 'Surenka'    

