from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from django.db import models



class User(AbstractUser):

    phone = models.CharField(max_length=15)
    days_off = models.PositiveSmallIntegerField(default=0)
    days_off_cumul = models.PositiveSmallIntegerField(default=0)
    permanent_contract = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Status(models.Model):

    name = models.CharField(max_length=30, unique=True)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):

    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    status = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['user', '-date']
        unique_together = [['user', 'status']]

status = [
    ######## Level 1 #################
    'boss', # patron
    # 'actionnaire', # ?
    'accountant', # comptable
    'hr', # rh
    # 'expert comptable', # expert accountant
    # 'ingénieur', # ? ingeneer
    # 'architecte', # ?
    # 'dessinateur industriel', # ?
    # 'géomètre', # ?
    # 'géomètre topographe', # ?
    'commercial', # commerciale
    # 'technico commercial', # commercial technician
    'repair operator', # chef sav
    # 'contremaître', # ?
    # 'conducteur des travaux', # site operator
    ######## Level 2 #################
    'receptionist', # standardiste
    'stock operator', #  chef atelier
    'electrotechnician', # electrotechnicien
    # 'electricien', # electrician
    # 'plombier', # ?
    # 'chauffagiste', # ?
    'repairman', # dépanneur
    'coppersmith', # chaudronnier
    'locksmith', # sérrurier
    'mason', # maçon
    # 'charpentier', # ?
    # 'menuisier', # ?
    # 'ébeniste', # ?
    # 'marquetier', # ?
    # 'carriste', # ?
    # 'conducteur engins de tp', # ?
    # 'plaquiste', # ?
    # 'carreleur', # ?
    # 'peintre', # ?
    'postman', # livreur
    'installer', # installateur
    'maintenance agent', # agent de maintenance
    # 'apprentis', # apprentices
    # 'stagière', # ?
    # 'fournisseur', # supplier
    'client',
]
