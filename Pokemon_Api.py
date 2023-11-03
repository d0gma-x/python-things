import requests
import json

url_api = 'https://pokeap.co/api/v2/pokemon/'

def main():
    while True:
        pokemon_name = input('Pokemon? >>> ').lower()
        pokemon_data_url = url_api + pokemon_name

        data = get_pokemon_data(pokemon_data_url)

        if data:
            print_pokemon_info(data)
        
        cont = input('¿Deseas busacr otro Pokémon? [Y/N] >>> ').lower()
        if cont != 'y':
            print('Good Bye!')
            break

def get_pokemon_data(url_pokemon=''):
    try:
        response = requests.get(url_pokemon)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Pokémon no encontrado.")
            return None
    except Exception as e:
        print(f"Error al obtener datos del Pokémon: {e}")
        return None

def print_pokemon_info(data):
    pokemon_type = [types['type']['name'] for types in data['types']]
    pokemon_abilities = [abilities['ability']['name'] for abilities in data['abilities']]

    print('---------------')
    print('name: ', (data['name']))
    print('types: ', pokemon_type)
    print('abilities: ', pokemon_abilities)
    print('height: ', data['height']/10,'m')
    print('weight: ', data['weight']/10,'kg')
    print('---------------')

if __name__ == '__main__':
    main()
