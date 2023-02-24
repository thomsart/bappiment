from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import NewUserCreationForm, NewUserChangeForm



class CustomUserAdmin(UserAdmin):
    add_form = NewUserCreationForm
    form = NewUserChangeForm
    model = User
    list_display = ['email', 'username',]

admin.site.register(User, CustomUserAdmin)