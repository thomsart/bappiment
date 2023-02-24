from django.shortcuts import render
from django.contrib.auth.models import User, Group

from .models import LegalEntity, ClientCompany, Installation
from .serializers import *

# Create your views here.
