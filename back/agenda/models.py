from datetime import date

from django.db import models

from home.models import User
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
    user = models.ForeignKey(User, null=True)
    user_state = models.ForeignKey(UserState, null=True)
    installation = models.ForeignKey(Installation, null=True)
    installation_state = models.ForeignKey(InstallationState, null=True)
    stock = models.ForeignKey(Stock, null=True)
    stock_state = models.ForeignKey(StockState, null=True)
    vehicle = models.ForeignKey(Vehicle, null=True)
    vehicle_state = models.ForeignKey(VehicleState, null=True)
    note = models.CharField(max_length=200, blank=True, default="")

    # faire en sorte que si tout est null ou que plus de un couple de foreign est présent, ca ne s'édite pas


class WorkSheet(models.model):

    date = models.DateField(auto_now_add=True)
    event = models.ForeignKey(Event)
    time = models.TimeField()
    user = models.ForeignKey(User)
    team = models.CharField(max_length=30, blank=True, default="")
    executed_job  = models.TextField(max_length=200, blank=True, default="")
    maintenance = models.JSONField(null=True)
