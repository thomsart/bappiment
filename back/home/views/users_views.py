from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from ..models import CustomUser, Status, Membership
from ..serializers import (LightCustomUserSerializer, HeavyCustomUserSerializer,
                           CreateCustomUserSerializer, UpdateCustomUserSerializer)
from ..permissions import IsActive, IsNotClient, IsCrudOnUserAllowed
from ..management.commands.datas import LANGUAGE
from ..management.commands.datas.user_status import STATUS



class CustomUserList(APIView):
    """  
    List all users, or create a new one.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
        IsCrudOnUserAllowed
    ]

    def get(self, request, format=None):

        users = CustomUser.objects.filter(is_superuser=False, is_staff=False, is_active=True)

        if int(request.user.hightest_level) >= 4:
            serializer = HeavyCustomUserSerializer(users, many=True)
        else:
            serializer = LightCustomUserSerializer(users, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        user = CreateCustomUserSerializer(data=request.data)
        if user.is_valid():
            user = user.save()
            serializer = HeavyCustomUserSerializer(user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetail(APIView):
    """
    Retrieve, update or delete(is_active=False) a user.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
        IsCrudOnUserAllowed
    ]

    def get_queryset(self):

        return CustomUser.objects.filter(is_superuser=False, is_staff=False, is_active=True)


    def get_object(self, pk):

        user = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, user)

        return user


    def get(self, request, pk, format=None):

        user = self.get_object(pk)

        if int(request.user.hightest_level) >= 4:
            serializer = HeavyCustomUserSerializer(user)
        else:
            serializer = LightCustomUserSerializer(user)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        user = self.get_object(pk)
        serializer = UpdateCustomUserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            heavy_user = HeavyCustomUserSerializer(user)

            return Response(heavy_user.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        user = self.get_object(pk)

        try:
            user.is_active = False
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except PermissionError:
            return Response(status=status.HTTP_403_FORBIDDEN)
