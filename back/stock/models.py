from django.db import models

from product.models import Product
from vehicle.models import Vehicle



class Stock(models.model):

    product = models.ForeignKey(Product)
    vehicle = models.ForeignKey(Vehicle, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
