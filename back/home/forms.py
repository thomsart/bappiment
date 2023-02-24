from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User



class NewUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')

class NewUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')