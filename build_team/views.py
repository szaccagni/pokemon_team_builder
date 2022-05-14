from unicodedata import name
import requests
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import JsonResponse
from json import JSONDecodeError 
import json


from .models import Team

# Create your views here.

# loads the home page with a complete list of games currently uploaded to the pokemon api
def index(request):
    games = create_games()
    return render(request, "build_team/home.html", {
        'games' : games
    })

class Team_Member:
    def __init__(self,name,id,sprite):
        self.name = name
        self.id = id
        self.sprite = sprite

    def __repr__(self):
        return self.name

def create_team(user,game):
    team = Team.objects.get(user_id=user,game=game)
    your_team = []
    poke_ids = team.pk_ids.split(",")
    poke_ids.pop()
    for id in poke_ids:
        sprite = get_sprite(id)
        name = get_poke_name(id)
        new_member = Team_Member(name,id,sprite)
        your_team.append(new_member)
    return your_team

# loads the page with your team complied for a specific game
def team_view(request):
    game = request.GET.get('games')
    # game = request.POST['games']
    game_data = create_games(game)
    try:
        team = Team.objects.get(user_id='1',game=game)
        has_team = True
        your_team = create_team('1',game)
    except:
        has_team = False
        your_team = []
    return render(request, "build_team/your_team.html", {
        'game' : game_data[0], 
        'regions' : game_data[0].region,
        'has_team' : has_team,
        'team' : your_team
    })

# loads the page where you can search for pokemon to add to your team
# pulls in the game data for the previously selected game
def build_team(request):
    game = request.GET.get('games')
    game_data = create_games(game)
    return render(request, "build_team/build_team.html", {
        'game' : game_data[0], 
        'regions' : game_data[0].region  
    })

# loads various data regarding the pokemon you searched for
def poke_search(request):
    game = request.GET.get('games')
    game_data = create_games(game)
    search = request.GET.get('searched').lower()
    url = 'https://pokeapi.co/api/v2/pokemon/' + search
    response = requests.get(url)
    try:
        poke_dict = response.json()
        poke_id = get_poke_id(search)
        sprite = get_sprite(search)
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
        appears_in_cur_game = check_game(poke_dict['game_indices'],game)
    except (JSONDecodeError, KeyError):
        return render(request, "build_team/build_team.html", {
            'game' : game_data[0], 
            'regions' : game_data[0].region,
            'error' : 'no results, check your spelling!',
        })
    else:
        return render(request, "build_team/build_team.html", {
            'pokemon' : search,
            'load_info_card' : True,
            'poke_id' : poke_id,
            'sprite' : sprite,
            'types' : types,
            'height' : height,
            'weight' : weight,
            'abilities' : abilities,
            'appears_in_cur_game' : appears_in_cur_game,
            'game' : game_data[0], 
            'regions' : game_data[0].region 
    })
    
# adding to the pokemon ids string for this users team for this game
def poke_add(request): 
    # data = json.loads(request.body)
    # pokemon = data.get("pokemon")
    # game = data.get("game")
    # pokemon = request.GET.get('pokemon_chosen')
    # game = request.GET.get('games')

    pokemon = request.POST['pokemon_chosen']
    game = request.POST['games']

    # if you cant get the team
    new_team_needed = False
    try:
        team = Team.objects.get(user_id='1',game=game)
    # create a new one
    except:    
        new_team_needed = True

    if new_team_needed:
        new_team = Team(
            user_id = '1',
            pk_ids = str(get_poke_id(pokemon)) + ",",
            pk_count = 1,
            game = game,
        )
        new_team.save()
        team = new_team
    else:
        # grab id of the last pokemon added to the team
        poke_ids = team.pk_ids.split(",")
        poke_ids.pop()
        last_added = poke_ids.pop()
        # id of pokemon currently being added
        adding = str(get_poke_id(pokemon))

        # check to make sure this pokemon was not just added
        if last_added != adding:
            team.pk_ids += adding + ","
            team.pk_count += 1
            team.save()
            
        return team_view(request)

    # not currently using this 
    # your_team = create_team('1',game)
    # game_data = create_games(game)
    # return render(request, "build_team/your_team.html", {
    #     'game' : game_data[0], 
    #     'regions' : game_data[0].region,
    #     'team' : your_team,
    #     'has_team' : True
    # })

# grabs the short description of an ability from the pokemon api   
def ability_effect(url):
    response = requests.get(url)
    ability_dict = response.json()
    effect_dict = ability_dict['effect_entries']
    for effect in effect_dict:
        if effect['language']['name'] == 'en':
            effect = effect['short_effect']
    return effect

# store data related to the current game you are playing
class Game:
    def __init__(self, game, region, gen, url):
        self.game = game
        self.region = region
        self.gen = gen
        self.url = url

    def __repr__(self):
        return self.game

# grab data for the game you are playing and store it in a Game object
def create_games(game=''):
    games = []
    if not game:
        url='https://pokeapi.co/api/v2/version-group?limit=50'
        response = requests.get(url)
        versions_grp_dict = response.json()
        results = versions_grp_dict['results']
        version_grp_urls = []
        for result in results:
            version_grp_urls.append(result['url'])
        for url in version_grp_urls:
            response = requests.get(url)
            vrsn_grp_dict = response.json()
            regions = []
            for region in vrsn_grp_dict['regions']:
                regions.append(region['name'])
            for version in vrsn_grp_dict['versions']:
                new_game = Game(version['name'],regions,vrsn_grp_dict['generation']['name'],version['url'])
                games.append(new_game)
    else:
        url='https://pokeapi.co/api/v2/version/' + game
        response = requests.get(url)
        version_dict = response.json()
        vrsn_grp_url = version_dict['version_group']['url']
        response = requests.get(vrsn_grp_url)
        vrsn_grp_dict = response.json()
        regions = []
        for region in vrsn_grp_dict['regions']:
            regions.append(region['name'])
        new_game = Game(game, regions,vrsn_grp_dict['generation']['name'],vrsn_grp_url)
        games.append(new_game)
    return games

# checks if the game you are playing appears in the list of games a particular pokemon appears in
# you cannot add a pokemon to your team if they do not appear in the game you are playing
def check_game(game_dict, game):
    present_in_games = []
    for item in game_dict:
        present_in_games.append(item['version']['name'])
    for item in present_in_games:
        if item == game:
            return True
    return False

# either the pokemon name or id can be passed here and you will get the same result
def get_sprite(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon
    response = requests.get(url)
    try:
        poke_dict = response.json()
        sprite = poke_dict['sprites']['front_default']
    except: 
        # unknown
        sprite = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/201.png'
    return sprite


def get_poke_id(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon
    response = requests.get(url)
    try: 
        poke_dict = response.json()
        poke_id = poke_dict['id']
    except:
        poke_id = '0'
    return poke_id


def get_poke_name(id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + id
    response = requests.get(url)
    try: 
        poke_dict = response.json()
        poke_name = poke_dict['name']
    except:
        poke_name = 'not found'
    return poke_name
