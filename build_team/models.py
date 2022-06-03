from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Team(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pk_ids = models.CharField(max_length=255)
    pk_count = models.IntegerField()
    game = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} - {self.game}'


class Leader(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=12)
    
    def __str__(self):
        return f'{self.name}'

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Reward(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Gym(models.Model):
    order = models.IntegerField()
    game = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE)
    reward = models.ManyToManyField(Reward)
    team = models.CharField(max_length=255)

    def __str__(self):
        return f'#{self.order} - {self.location}'
    
    
