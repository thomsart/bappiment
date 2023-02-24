from django.shortcuts import render
from django.contrib.auth.models import Group

from .models import LegalEntity, Client, Installation
from .serializers import *

# Create your views here.
