from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("your_team", views.team_view, name="team"),
    path("buildteam", views.build_team, name="buildteam"),
    path("poke_search", views.poke_search, name="pokesearch"),
    path("poke_add", views.poke_add, name="pokeadd")
]