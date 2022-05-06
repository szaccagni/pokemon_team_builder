from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("your_team", views.team, name="team"),
    path("buildteam/<str:game>", views.build_team, name="buildteam"),
    path("poke_search/<str:game>", views.poke_search, name="pokesearch"),
    path("poke_add/<str:pokemon>/<str:game>", views.poke_add, name="pokeadd")
]