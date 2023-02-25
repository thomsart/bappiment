from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions

from .models import CustomUser
from .serializers import CustomUserSerializer, GroupSerializer



class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# vue page entreprise
# permission [None]

# vues generiques des users avec status (ou selon status)
# permission []

# vues generiques des status
# permission []

# vue compte
# permission []

# creation/suppression(is_active=False) user
# permission ['superuser', 'patron', ]

# ajout/suppression de status a un user
# permission ['patron']