from datetime import date
from django.db import models

from home.models import CustomUser



class LegalEntity(models.Model):

    name = models.CharField(max_length=15, unique=True)


class Client(models.Model):

    legal_entity = models.ForeignKey(LegalEntity, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, unique=True)
    siren = models.CharField(max_length=9, unique=True, blank=True, null=True)
    siret = models.CharField(max_length=14, unique=True, blank=True, null=True)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    nb_street = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    is_still_client = models.BooleanField(default=True)
    contact = models.ForeignKey(CustomUser, models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['legal_entity', 'name']
        unique_together = [['legal_entity', 'name']]


class Installation(models.Model):

    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    nb_street = models.CharField(max_length=10)
    maps = models.ImageField(null=True)
    photo = models.ImageField(null=True)
    date_delivering = models.DateField(default=date.today)
    maintenance_nb  = models.PositiveSmallIntegerField(default=0)
    info = models.TextField(max_length=200, blank=True, default="")
    is_still_in_service = models.BooleanField(default=True)

    class Meta:
        ordering = ['client']