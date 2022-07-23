import requests
# from pprint import pprint

def super_hero():
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    hero_dict = {}
    hero_str = ', '.join(hero_list)
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url=url).json()
    for shero in hero_list:
        for hero in response:
            if hero['name'] == shero:
                hero_dict[hero['powerstats']['intelligence']] = hero['name']

    print(f'Intelligence superhero {hero_dict[max(hero_dict.keys())]} = {max(hero_dict.keys())} of the {hero_str}')
    # pprint(hero_dict)

if __name__ == '__main__':
    super_hero()