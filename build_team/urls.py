from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("", views.index, name="index"),
    path("allTeams", views.allTeams, name="allTeams"),
    path("your_team", views.team_view, name="team"),
    path("buildteam", views.build_team, name="buildteam"),
    path("poke_search", views.poke_search, name="pokesearch"),
    path("poke_add", views.poke_add, name="pokeadd"),
    path("poke_remove", views.poke_remove, name="pokeremove")
]