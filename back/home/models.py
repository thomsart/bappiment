from django.db import models
from django.contrib.auth.models import AbstractUser


from client.models import Client


class User(AbstractUser):

    phone = models.CharField(max_length=15)
    client = models.Choices(Client, blank=True, default="")


    def __str__(self):
        return self.email

user_groups = [
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
    'contact_fournisseur', # supplier
    'contact_client', # client
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