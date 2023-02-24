from datetime import date

from django.db import models



class LegalEntity(models.model):

    entity = models.CharField(max_length=15, unique=True)


class Client(models.Model):

    legal_entity = models.Choices(LegalEntity)
    name = models.CharField(max_length=50, unique=True)
    siren = models.CharField(max_length=9, unique=True, blank=True, null=True)
    siret = models.CharField(max_length=14, unique=True, blank=True, null=True)
    address = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)


class Installation(models.model):

    address = models.CharField(max_length=100)
    map = models.ImageField(null=True)
    photo = models.ImageField(null=True)
    date_delivering = models.DateField(default=date.today)
    maintenance_nb  = models.PositiveSmallIntegerField(default=0)
    info = models.CharField(max_length=200, blank=True, default="")
    client = models.ForeignKey(Client)