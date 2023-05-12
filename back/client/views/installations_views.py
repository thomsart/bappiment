from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from ..models import LegalEntity
from ..serializers import LegalEntitySerializer
from home.permissions import IsActive, IsNotClient



class InstallationList(APIView):
    ...


class InstallationDetail(APIView):
    ...
