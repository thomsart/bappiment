from django.db import models

from product.models import Product
from vehicle.models import Vehicle



class Stock(models.model):

    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
