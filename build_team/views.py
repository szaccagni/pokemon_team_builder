import requests
from django.shortcuts import redirect, render
from json import JSONDecodeError 
from .models import Game, Team, Gym, Leader
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db import IntegrityError

# function to check that user is logged in
# used via a decorator for more functions
def verify_login(func):
    def logged_in(request):
        if request.user.is_authenticated:
            return func(request)
        else:
            return redirect('login')
    return logged_in


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first = request.POST["first_name"]
        last = request.POST["last_name"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "build_team/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=first, last_name=last)
            user.save()
        except IntegrityError:
            return render(request, "build_team/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "build_team/register.html")


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "build_team/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "build_team/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


# loads the home page with a complete list of games currently uploaded to the pokemon api
@verify_login
def index(request):
    games = Game.objects.all()
    return render(request, "build_team/home.html", {
        'games' : games
    })

# grab all teams already created for a specific user
@verify_login
def allTeams(request):
    teams = Team.objects.all().filter(user=request.user)
    return render(request, 'build_team/allTeams.html', {
        'teams' : teams
    })

# used to organize and store individual pokemon information pulled via api
class Team_Member:
    def __init__(self,name,id,sprite):
        self.name = name
        self.id = id
        self.sprite = sprite

    def __repr__(self):
        return self.name

# pull pokemon info for user or gym leader
def create_team(user,game):
    team = Team.objects.get(user=user,game=game)
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
@verify_login
def team_view(request,error=''):
    game_txt = request.GET.get('games')
    game = Game.objects.get(name=game_txt)
    try:
        team = Team.objects.get(user=request.user,game=game)
        has_team = True
        your_team = create_team(request.user,game)
        team_count = len(your_team)
    except:
        has_team = False
        your_team = []
        team_count = 0
    return render(request, "build_team/your_team.html", {
        'error' : error,
        'game' : game, 
        'has_team' : has_team,
        'team' : your_team,
        'team_count' : team_count
    })

# loads the page where you can search for pokemon to add to your team
# pulls in the game data for the previously selected game
@verify_login
def build_team(request):
    game = request.GET.get('games')
    game_data = Game.objects.get(name=game)
    return render(request, "build_team/build_team.html", {
        'game' : game_data, 
    })

# loads various data regarding the pokemon you searched for
@verify_login
def poke_search(request):
    game = request.GET.get('games')
    game_data = Game.objects.get(name=game)
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
            'game' : game_data,
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
            'game' : game_data
    })
    
# adding to the pokemon ids string for this users team for this game
@verify_login
def poke_add(request): 
    pokemon = request.POST['pokemon_chosen']
    game_txt = request.POST['games']
    game = Game.objects.get(name=game_txt)

    # if you cant get the team
    new_team_needed = False
    try:
        team = Team.objects.get(user=request.user,game=game)
    # create a new one
    except:    
        new_team_needed = True

    if new_team_needed:
        new_team = Team(
            user = request.user,
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


# remove a specific pokemon from a team
@verify_login
def poke_remove(request):
    poke_id = request.POST['poke_id']
    game_txt = request.POST['games']
    game = Game.objects.get(name=game_txt)
    try:
        team = Team.objects.get(user=request.user,game=game)
        error = ''
    except:
        error = 'error, please try again'
        return team_view(request, error)
    
    if not error:
        pk_ids = team.pk_ids
        pk_ids_list = pk_ids.split(",")
        pk_ids_list.pop()
        # check to make sure they aren't reloading the page
        if poke_id in pk_ids_list:
            r_index = pk_ids_list.index(poke_id)
            pk_ids_list.pop(r_index)
            # new list of ids without the id that is being removed
            pk_ids_str = ','.join(pk_ids_list) + ',' 
            team.pk_count -= 1
            team.pk_ids = pk_ids_str
            team.save()
            
            return team_view(request)
        else:
            return team_view(request)



# grabs the short description of an ability from the pokemon api   
def ability_effect(url):
    response = requests.get(url)
    ability_dict = response.json()
    effect_dict = ability_dict['effect_entries']
    for effect in effect_dict:
        if effect['language']['name'] == 'en':
            effect = effect['short_effect']
    return effect

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

# load gym leader information for a specific game
@verify_login
def battle(request):
    game = request.GET.get('games')
    game_data = Game.objects.get(name=game)
    leader_name = request.GET.get('leader')
    error = ''
    team = []
    gyms = []
    try:
        gyms = Gym.objects.all().filter(game=game_data)
    except:
        error = "there was an error"
    
    if not leader_name:
        leader = ''
    else:
        leader = Leader.objects.get(name=leader_name)
        gym = Gym.objects.get(game=game_data,leader=leader)
        poke_ids = gym.team.split(",")
        poke_ids.pop()
        for id in poke_ids:
            sprite = get_sprite(id)
            name = get_poke_name(id)
            new_member = Team_Member(name,id,sprite)
            team.append(new_member)

    return render(request, 'build_team/gyms.html', {
        'error' : error,
        'gyms':gyms,
        'game' : game_data,
        'leader':leader,
        'team' : team
    })

# determin if a user's team would win against a specific gym leader
@verify_login
def battle_leader(request):
    game = request.GET.get('games')
    game_data = Game.objects.get(name=game)
    leader_name = request.GET.get('leader')
    leader = Leader.objects.get(name=leader_name)
    gym = Gym.objects.get(leader=leader,game=game_data)
    team = Team.objects.get(user=request.user,game=game_data)

    # calc number of pokemon the gym leader has
    gym_pk_count = gym.team.count(',')

    # calc probably based on number of team members 
    member_prob = ((team.pk_count - gym_pk_count) / team.pk_count) * 100

    if member_prob > 50: 
        outcome = 'winner'
    else: 
        outcome = 'looser'

    return render(request, 'build_team/battleOutcome.html' , {
        'outcome' : outcome,
        'leader' : leader_name,        
        'game' : game_data,
    })
    
