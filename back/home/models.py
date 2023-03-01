from django.contrib.auth.models import AbstractUser

from django.db import models



class CustomUser(AbstractUser):

    phone = models.CharField(max_length=15)
    days_off = models.PositiveSmallIntegerField(default=0)
    days_off_cumul = models.PositiveSmallIntegerField(default=0)
    permanent_contract = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class CustomUserStatus(models.Model):

    status = models.CharField(max_length=10, unique=True)
    members = models.ManyToManyField(
        CustomUser, through='Membership', through_fields=('status', 'user'),)

class Membership(models.Model):

    status = models.ForeignKey(CustomUserStatus, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(CustomUser, models.SET_NULL, blank=True, null=True)
    inviter = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="Membership_invites",)


user_status = [

############ Level 1 #######################################
############ Level 1 #######################################
############ Level 1 #######################################

    'boss', # patron
    # 'actionnaire', # ?
    'accountant', # comptable
    'Hr', # rh
    # 'expert_comptable', # expert accountant
    # 'ingénieur', # ? ingeneer
    # 'architecte', # ?
    # 'dessinateur_industriel', # ?
    # 'géomètre', # ?
    # 'géomètre_topographe', # ?
    'commercial', # commerciale
    # 'technico_commercial', # commercial technician
    'repair_operator', # chef_sav
    # 'contremaître', # ?
    # 'conducteur_des_travaux ', # site_operator

############ Level 2 #######################################
############ Level 2 #######################################
############ Level 2 #######################################

    'receptionist', # standardiste
    'stock_operator', #  chef_atelier
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
    # 'conducteur_engins_de_tp', # ?
    # 'plaquiste', # ?
    # 'carreleur', # ?
    # 'peintre', # ?
    'postman', # livreur
    'installer', # installateur
    'maintenance_agent', # agent_de_maintenance
    # 'apprentis', # apprentices
    # 'stagière', # ?
    # 'fournisseur', # supplier
    'client',
]
