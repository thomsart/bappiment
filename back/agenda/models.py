from datetime import date

from django.db import models

from home.models import User, Client
from client.models import Installation
from stock.models import Stock
from vehicle.models import Vehicle



class UserState(models.model):

    state = models.CharField(max_length=30, unique=True)


class InstallationState(models.model):

    state = models.CharField(max_length=30, unique=True)


class StockState(models.model):

    state = models.CharField(max_length=30, unique=True)


class VehicleState(models.model):

    state = models.CharField(max_length=30, unique=True)


class Event(models.model):

    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    user_state = models.ForeignKey(UserState, models.SET_NULL, blank=True, null=True)
    installation = models.ForeignKey(Installation, models.SET_NULL, blank=True, null=True)
    installation_state = models.ForeignKey(InstallationState, models.SET_NULL, blank=True, null=True)
    stock = models.ForeignKey(Stock, models.SET_NULL, blank=True, null=True)
    stock_state = models.ForeignKey(StockState, models.SET_NULL, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, models.SET_NULL, blank=True, null=True)
    vehicle_state = models.ForeignKey(VehicleState, models.SET_NULL, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, default="")

    # il faut qu'il y est un seul couple != null


class WorkSheet(models.model):

    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    installation = models.ForeignKey(Installation, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, models.SET_NULL, blank=True, null=True)
    time = models.TimeField()
    executed_job = models.TextField(max_length=200, blank=True, default="")
    maintenance = models.JSONField(null=True)
    team = models.CharField(max_length=30, blank=True, default="")

    # eviter que executed_job et maintenance soient tout les deux ""
