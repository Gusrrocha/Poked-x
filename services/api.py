# chamada do pokéAPI

import httpx
from model.pokemon import Pokemon

MAX_POKEMONS = 10

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'
params = {'limit': MAX_POKEMONS}

def carregar_pokemons():
    request = httpx.get(BASE_URL, params=params)
    response = request.json() # retorna um dicionário
    return response

def get_pokemon(url):
    req = httpx.get(url)
    res = req.json()
    return res

def load():
    res = carregar_pokemons()
    lista_pokemons = []
    lista_resultados = res['results']
    for poke in lista_resultados:
        nome = poke['name']
        info_poke = get_pokemon(poke['url'])
        id = info_poke['id']
        foto_url = info_poke['sprites']['other']['dream_world']['front_default']
        tipos = info_poke['types']

        print(f'{id} - {nome} - {foto_url} - {tipos}')
        
        #cria o objeto pokemon
        novo_pokemon = Pokemon(id, nome, foto_url, tipos)
        lista_pokemons.append(novo_pokemon)

    return lista_pokemons