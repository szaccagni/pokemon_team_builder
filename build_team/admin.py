from django.contrib import admin
from .models import Game,Team,Leader,Location,Reward,Gym

class GameAdmin(admin.ModelAdmin):
    list_display = ("name","region","gen", "gen_roman", "url", "group_name", "color", "has_gyms")

class RewardAdmin(admin.ModelAdmin):
    list_display = ("name","type")

class GymAdmin(admin.ModelAdmin):
    # admin.ModelAdmin.save_as = True
    list_display = ("order","location","leader","game")

class TeamAdmin(admin.ModelAdmin):
    list_display = ("user","pk_count","pk_ids","game")

# Register your models here.
admin.site.register(Game,GameAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Leader)
admin.site.register(Location)
admin.site.register(Reward,RewardAdmin)
admin.site.register(Gym,GymAdmin)
