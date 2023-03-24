from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from django.db import models
from .managers import CustomUserManager



class CustomUser(AbstractUser):

    username = None
    email = models.EmailField('email address', unique=True)
    phone = models.CharField(max_length=15)
    days_off = models.PositiveSmallIntegerField(default=0)
    days_off_cumul = models.PositiveSmallIntegerField(default=0)
    hightest_level = models.CharField(max_length=1, default="0")
    permanent_contract = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Status(models.Model):

    name = models.CharField(max_length=30, unique=True)
    level = models.CharField(max_length=1)
    members = models.ManyToManyField(CustomUser, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):

    date = models.DateField(auto_now=True)
    user = models.ForeignKey(CustomUser, models.SET_NULL, blank=True, null=True)
    status = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['user', '-date']
        unique_together = [['user', 'status']]
