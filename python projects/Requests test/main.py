import requests
token = '013ed52b598d866b2e96dda329f68959' #мой токен
host = 'https://api.pokemonbattle.me:9104' #покемон хост

"""response_create_pokemons = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "Арбузик",
    "photo": "https://dolnikov.ru/pokemons/albums/077.png"
}, headers = {'Content-type' : 'application/json', 'trainer_token': token})
print(response_create_pokemons.text)""" #Создание покемона

"""response_kill_pokemons = requests.post('https://api.pokemonbattle.me:9104/pokemons/kill', json={
    "pokemon_id": "5988"
}, headers= {'Content-type': 'application/json', 'trainer_token': token})
print(response_kill_pokemons.text)""" #Убить покемона


"""response_change_pokemons = requests.put('https://api.pokemonbattle.me:9104/pokemons', json={
    "pokemon_id": "5993",
    "name": "Аркадий",
    "photo": "https://dolnikov.ru/pokemons/albums/077.png"
}, headers= {'Content-type': 'application/json','trainer_token': token})
print(response_change_pokemons.text)""" #Сменить имя и картинку покемона

"""response_add_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "5991"
  }, headers= {'Content-type': 'application/json','trainer_token': token})
print(response_add_pokeball.text)""" #Поймать покемона в покеболл


 



 