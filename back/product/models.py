from django.db import models

from client.models import Installation



class ProductFamily(models.Model):

    family = models.CharField(max_length=30, unique=True)


class ProductBrand(models.Model):

    brand = models.CharField(max_length=30, unique=True)


class Product(models.Model):

    family = models.ForeignKey(ProductFamily, on_delete=models.PROTECT)
    brand = models.ForeignKey(ProductBrand, on_delete=models.PROTECT)
    ref = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=20, blank=True, default="")
    dimension = models.JSONField(null=True)
    total_bought = models.PositiveIntegerField(default=0)
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    sale = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    info = models.TextField(max_length=200, blank=True, default="")
    doc = models.FileField(null=True)
    info = models.TextField(max_length=200, blank=True, default="")


class InstallationProduct(models.Model):

    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    installation = models.ForeignKey(Installation, models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
