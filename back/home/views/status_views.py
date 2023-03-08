from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from ..models import Status
from ..serializers import StatusSerializer
from ..permissions import IsActive, IsNotClient


class StatusList(APIView):
    """
    List all status.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
    ]

    def get(self, request, format=None):

        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)

        return Response(serializer.data)