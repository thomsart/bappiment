from django.db import models
# from django.contrib.auth.models import User

from home.models import CustomUser

class Vehicle(models.Model):

    model = models.CharField(max_length=10)
    date  = models.DateField(auto_now_add=True)
    licence_plate = models.CharField(max_length=15, unique=True)
    km  = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    registration_card = models.ImageField(null=True)
    user = models.ForeignKey(CustomUser, models.SET_NULL, blank=True, null=True)