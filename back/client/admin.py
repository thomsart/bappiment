from django.contrib import admin

from .models import LegalEntity, Client
from home.models import CustomUser



admin.site.register(LegalEntity, CustomUser)
admin.site.register(Client, CustomUser)
