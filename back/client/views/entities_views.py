from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from ..models import LegalEntity
from ..serializers import LegalEntitySerializer
from home.permissions import IsActive, IsNotClient


class LegalEntityViews(viewsets.ReadOnlyModelViewSet):
    """
    List all status or get a specific one.
    """

    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
    ]