from datetime import date

from django.db import models

from home.models import User
from client.models import Client, Installation
from stock.models import Stock
from vehicle.models import Vehicle



class UserState(models.Model):

    state = models.CharField(max_length=30, unique=True)


class InstallationState(models.Model):

    state = models.CharField(max_length=30, unique=True)


class ProductState(models.Model):

    state = models.CharField(max_length=30, unique=True)


class VehicleState(models.Model):

    state = models.CharField(max_length=30, unique=True)


class Event(models.Model):

    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    user_state = models.ForeignKey(UserState, models.SET_NULL, blank=True, null=True)
    installation = models.ForeignKey(Installation, models.SET_NULL, blank=True, null=True)
    installation_state = models.ForeignKey(InstallationState, models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Stock, models.SET_NULL, blank=True, null=True)
    product_state = models.ForeignKey(ProductState, models.SET_NULL, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, models.SET_NULL, blank=True, null=True)
    vehicle_state = models.ForeignKey(VehicleState, models.SET_NULL, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, default="")

    # il faut qu'il y est un seul couple != null


class WorkSheet(models.Model):

    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    installation = models.ForeignKey(Installation, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, models.SET_NULL, blank=True, null=True)
    time = models.TimeField()
    executed_job = models.TextField(max_length=200, blank=True, default="")
    maintenance = models.JSONField(null=True)
    team = models.CharField(max_length=30, blank=True, default="")
    note = models.TextField(max_length=200, blank=True, default="")

    # eviter que executed_job et maintenance soient tout les deux ""
