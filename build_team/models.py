from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Team(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pk_ids = models.CharField(max_length=255)
    pk_count = models.IntegerField()
    game = models.CharField(max_length=255)