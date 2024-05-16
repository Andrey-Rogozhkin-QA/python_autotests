import requests
import pytest

URL='https://api.pokemonbattle.me/v2'
TOKEN='511b438ad2a0c41a4aa9debda3b4d2a7'
HEADER={'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID='2582'

def test_status_code():
    response=requests.get(url=f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response.status_code==200

def test_part_of_response():
    response_get=requests.get(url=f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"]=='AndreyRGK'

@pytest.mark.parametrize('key, value', [('trainer_name', 'AndreyRGK'), ('id', '2582')])
def test_parametrize(key,value):
    response_parametrize=requests.get(url=f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key]==value