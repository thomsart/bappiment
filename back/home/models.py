from django.contrib.auth.models import AbstractUser

from django.db import models



class User(AbstractUser):

    phone = models.CharField(max_length=15)
    days_off = models.PositiveSmallIntegerField(default=0)
    days_off_cumul = models.PositiveSmallIntegerField(default=0)
    permanent_contract = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class UserStatus(models.Model):

    status = models.CharField(max_length=30, unique=True)
    members = models.ManyToManyField(
        User, through='Membership', through_fields=('status', 'user'),)

class Membership(models.Model):

    status = models.ForeignKey(UserStatus, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    date = models.DateField(auto_now=True)
    inviter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Membership_invites",)


user_status = [

############ Level 1 #######################################
############ Level 1 #######################################
############ Level 1 #######################################

    'boss', # patron
    # 'actionnaire', # ?
    'accountant', # comptable
    'Hr', # rh
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

############ Level 2 #######################################
############ Level 2 #######################################
############ Level 2 #######################################

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
