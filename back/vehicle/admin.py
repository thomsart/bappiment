from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Vehicle



admin.site.register(Vehicle, UserAdmin)
