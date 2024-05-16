import requests

URL='https://api.pokemonbattle.me/v2'
TOKEN='511b438ad2a0c41a4aa9debda3b4d2a7'
HEADER={'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_pokemon={
    "name": "Qwerty",
    "photo": "https://dolnikov.ru/pokemons/albums/004.png"
}

body_name={
    "pokemon_id":"27347",
    "name":"NEW",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_pokeball={
    "pokemon_id":"27344",
}

'''response_pokemon=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemon)
print(response.text)'''

'''response_name=requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_name)
print(response_name.text)'''

response_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(response_pokeball.text)
