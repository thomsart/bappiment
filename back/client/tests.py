from django.test import TestCase
from django.contrib.auth.models import User, Group

from .models import LegalEntity, ClientCompany, Installation
from .serializers import *
from .views import *

# Create your tests here.
