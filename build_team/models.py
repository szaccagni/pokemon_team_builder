from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Team(models.Model):
    user_id = models.CharField(max_length=3)
    p1_id = models.CharField(max_length=3)
    p2_id = models.CharField(max_length=3)
    p3_id = models.CharField(max_length=3)
    p4_id = models.CharField(max_length=3)
    p5_id = models.CharField(max_length=3)
    p6_id = models.CharField(max_length=3)
