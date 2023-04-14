from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from ..models import Status
from ..serializers import StatusSerializer
from ..permissions import IsActive, IsNotClient


class StatusViews(viewsets.ReadOnlyModelViewSet):
    """
    List all status or get a specific one.
    """

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
    ]
