from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("buildteam", views.build_team, name="buildteam"),
    path("poke_search", views.poke_search, name="pokesearch")
]