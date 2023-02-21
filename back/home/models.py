from django.db import models

# Create your models here.

# The application use the 'django.contrib.auth.models' with 'User' and 'Group'
groups_are = [
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

notifications = [
    "impayé",
    "retard",
    "épuisé",
    "contôle_technique",
    "révision",
]