from django.db import models



class Supplier(models.Model):

    name = models.CharField(max_length=50, unique=True)
    siren = models.CharField(max_length=9, unique=True, blank=True, null=True)
    siret = models.CharField(max_length=14, unique=True, blank=True, null=True)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    nb_street = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)


class Contact(models.Model):

    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)