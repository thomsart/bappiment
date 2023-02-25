from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUserStatus(models.Model):

    status = models.CharField(max_length=10, unique=True)


class CustomUser(AbstractUser):

    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.email

class CustomUserWithStatus(models.Model):

    user = models.ForeignKey(CustomUser, models.SET_NULL, blank=True, null=True)
    status = models.ForeignKey(CustomUserStatus, models.SET_NULL, blank=True, null=True)


user_status = [
    'patron', # cto
    'actionnaire', # ?
    'comptable', # accountant
    'expert_comptable', # expert accountant
    'ingénieur', # ? ingeneer
    'architecte', # ?
    'dessinateur_industriel', # ?
    'géomètre', # ?
    'géomètre_topographe', # ?
    'commerciale', # commercial
    'technico_commercial', # commercial technician
    'standardiste', # receptionist
    'conducteur_des_travaux ', # site_operator
    'chef_sav', # repair_operator
    'chef_atelier', #  stock_operator
    'contremaître', # ?
    'electrotechnicien', # electrotechnician
    'electricien', # electrician
    'plombier', # ?
    'chauffagiste', # ?
    'dépanneur', # repairman
    'chaudronnier', # coppersmith
    'sérrurier', # locksmith
    'maçon', # mason
    'charpentier', # ?
    'menuisier', # ?
    'ébeniste', # ?
    'marquetier', # ?
    'carriste', # ?
    'conducteur_engins_de_tp', # ?
    'plaquiste', # ?
    'carreleur', # ?
    'peintre', # ?
    'livreur', # postman
    'installateur', # installer
    'agent_de_maintenance', # maintenance_agent
    'apprentis', # apprentices
    'stagière', # ?
    'fournisseur', # supplier
    'client', # client
]
