from django.contrib.auth.models import AbstractUser
from django.db import models



class Status(models.Model):

    status = models.CharField(max_length=10, unique=True)


class CustomUser(AbstractUser):

    phone = models.CharField(max_length=15)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)

    def __str__(self):
        return self.email

user_status = [
    'comptable', # accountant
    'commerciale', # commercial
    'standardiste', # receptionist
    'conducteur_travaux ', # site_operator
    'chef_sav', # repair_operator
    'chef_atelier', #  stock_operator
    'contremaître', # ?
    'electrotechnicien', # electrotechnician
    'electricien', # electrician
    'dépanneur', # repairman
    'maçon', # mason
    'chaudronnier', # coppersmith
    'sérrurier', # locksmith
    'livreur', # postman
    'poseur', # installer
    'agent_maintenance', # maintenance_agent
    'apprentis', # apprentices
    'fournisseur', # supplier
    'client', # client
]

user_state = [
    "chantier",
    "déplacement chantier",
    "dépannage",
    "déplacement dépannage",
    "maintenace",
    "déplacement maintenance",
    "livraison",
    "congé",
    "arrêt maladie",
    "accident de travail",
    "retard",
    "absent",
    "réunion",
    "rdv",
    "bbq",
]

installation_state = [
    "retard",
    "chantier",
    "avarie",
    "panne",
    "maintenance",
    "attente paiement",
    "fonctionne",
]

product_family = [
    "bureautique",
    "epi",
    "outillage",
    "électroportatif",
    "électricité",
    "électronique",
    "sécurité",
    "mécanique",
    "pneumatique",
    "entretien",
    "maçonnerie",
    "peinture",
    "métal",
    "consommable",
]

product_state = [
    "rupture",
    "hs",
]

vehicle_state = [
    "contôle technique",
    "révision",
    "accident",
]