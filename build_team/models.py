from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Team(models.Model):
    user_id = models.CharField(max_length=3)
    pk_ids = models.CharField(max_length=255)
    pk_count = models.IntegerField()
    game = models.CharField(max_length=255)