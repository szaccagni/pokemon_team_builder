from operator import mod
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255,unique=True)
    region = models.CharField(max_length=255)
    gen = models.CharField(max_length=255)
    gen_roman = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    has_gyms = models.BooleanField()
    color = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Team(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pk_ids = models.CharField(max_length=255)
    pk_count = models.IntegerField()
    game = models.ForeignKey(Game,on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user} - {self.game}'


class Leader(models.Model):
    name = models.CharField(max_length=255,unique=True)
    color = models.CharField(max_length=12)
    
    def __str__(self):
        return f'{self.name}'

class Location(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return f'{self.name}'

class Reward(models.Model):
    name = models.CharField(max_length=255,unique=True)
    type = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Gym(models.Model):
    order = models.IntegerField()
    game_txt = models.CharField(max_length=255,null=True)
    game = models.ForeignKey(Game,on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE)
    reward = models.ManyToManyField(Reward)
    team = models.CharField(max_length=255)

    def __str__(self):
        return f'#{self.order} - {self.location}'
    
    
