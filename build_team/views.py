import requests
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from json import JSONDecodeError 

import requests

# Create your views here.

def index(request):
    return render(request, "build_team/your_team.html")

def build_team(request):
    return render(request, "build_team/build_team.html")


def poke_search(request):
    search = request.GET.get('searched').lower()
    url = 'https://pokeapi.co/api/v2/pokemon/' + search
    response = requests.get(url)
    try:
        poke_dict = response.json()
        poke_id = poke_dict['id']
        sprite = poke_dict['sprites']['front_default']
        types = []
        for type in poke_dict['types']:
            types.append(type['type']['name'])
        height = round(poke_dict['height'] / 3.048, 2)
        weight = round((poke_dict['weight'] * 100) / 454)
        abilities = []
        for ability in poke_dict['abilities']:
            abilities.append(ability['ability'])
        for ability in abilities:
            ability['description'] = ability_effect(ability['url'])
        location = poke_dict['location_area_encounters']
    except (JSONDecodeError, KeyError):
        return render(request, "build_team/build_team.html", {
            'error' : 'no results, check your spelling!'
        })
    else:
        return render(request, "build_team/build_team.html", {
            'load_info_card' : True,
            'poke_id' : poke_id,
            'sprite' : sprite,
            'types' : types,
            'height' : height,
            'weight' : weight,
            'abilities' : abilities,
            'location' : location
    })
    
def ability_effect(url):
    response = requests.get(url)
    ability_dict = response.json()
    effect_dict = ability_dict['effect_entries']
    for effect in effect_dict:
        if effect['language']['name'] == 'en':
            effect = effect['short_effect']
    return effect