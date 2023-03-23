from django.db import models

# from client.models import Installation



# class ProductFamily(models.Model):

#     family = models.CharField(max_length=30, unique=True)


# class ProductBrand(models.Model):

#     brand = models.CharField(max_length=30, unique=True)


# class Product(models.Model):

#     family = models.ForeignKey(ProductFamily, on_delete=models.PROTECT)
#     brand = models.ForeignKey(ProductBrand, on_delete=models.PROTECT)
#     ref = models.CharField(max_length=50, unique=True)
#     dimension = models.JSONField(null=True) # characteristic = {height:
#                                             #                   width:
#                                             #                   thickness:
#                                             #                   voltage: "24vac", "12vdc"
#                                             #                   material:
#                                             #                   color:
#                                             #                   info: "ce produit n'est pas compatible avec ..."
#                                             #                   etc}
#     total_bought = models.PositiveIntegerField(default=0)
#     cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
#     sale = models.DecimalField(max_digits=8, decimal_places=2, default=0)
#     doc = models.FileField(null=True)


# class InstallationProduct(models.Model):

#     installation = models.ForeignKey(Installation, models.SET_NULL, blank=True, null=True)
#     product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
#     quantity = models.PositiveSmallIntegerField(default=1)
