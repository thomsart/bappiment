from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import LegalEntity, Client



admin.site.register(LegalEntity, UserAdmin)
admin.site.register(Client, UserAdmin)
