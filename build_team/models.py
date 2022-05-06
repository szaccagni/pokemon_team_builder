from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# there is a better way to do this, make it more modular
# i am going to fix this
class Team(models.Model):
    user_id = models.CharField(max_length=3)
    p1 = models.CharField(max_length=255)
    p1_id = models.CharField(max_length=255)
    p1_sprite = models.CharField(max_length=255)
    p2 = models.CharField(max_length=255, blank=True)
    p2_id = models.CharField(max_length=255,blank=True)
    p2_sprite = models.CharField(max_length=255,blank=True)
    p3 = models.CharField(max_length=255,blank=True)
    p3_id = models.CharField(max_length=255,blank=True)
    p3_sprite = models.CharField(max_length=255,blank=True)
    p4 = models.CharField(max_length=255,blank=True)
    p4_id = models.CharField(max_length=255,blank=True)
    p4_sprite = models.CharField(max_length=255,blank=True)
    p5 = models.CharField(max_length=255,blank=True)
    p5_id = models.CharField(max_length=255,blank=True)
    p5_sprite = models.CharField(max_length=255,blank=True)
    p6 = models.CharField(max_length=255,blank=True)
    p6_id = models.CharField(max_length=255,blank=True)
    p6_sprite = models.CharField(max_length=255,blank=True)
    game = models.CharField(max_length=255)