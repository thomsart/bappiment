from django.db import models

from client.models import Installation



class ProductFamily(models.model):

    family = models.CharField(max_length=30, unique=True)


class ProductBrand(models.model):

    brand = models.CharField(max_length=30, unique=True)


class Product(models.model):

    family = models.Choices(ProductFamily)
    brand = models.Choices(ProductBrand)
    ref = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=20, blank=True, default="")
    dimension = models.JSONField(null=True)
    total_bought = models.PositiveSmallIntegerField(default=0)
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    sale = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    info = models.TextField(max_length=200, blank=True, default="")
    doc = models.FileField(null=True) # ou FilePathField()
    info = models.TextField(max_length=200, blank=True, default="")


class InstallationProduct():

    client_installation = models.ForeignKey(Installation)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField(default=1)