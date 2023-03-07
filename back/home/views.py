from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .models import User, Status, Membership
from .serializers import (
    StatusSerializer,
    LightUserSerializer, HeavyUserSerializer, CreateUserSerializer,
    MembershipSerializer, CreateMembershipSerializer
)
from .permissions import IsActive, IsNotClient,  IsActionAllowed


########################## STATUS #############################################
########################## STATUS #############################################
########################## STATUS #############################################


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


########################## USER ###############################################
########################## USER ###############################################
########################## USER ###############################################


class UserList(APIView):
    """
    List all users, or create a new one.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
        IsActionAllowed,
    ]

    def get(self, request, format=None):

        users = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)

        if int(request.user.hightest_level) >= 4:
            serializer = HeavyUserSerializer(users, many=True)
        else:
            serializer = LightUserSerializer(users, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete(is_active=False) a user.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
        IsActionAllowed,
    ]

    def get_object(self, pk):

        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        user = self.get_object(pk)

        if int(request.user.hightest_level) >= 3:
            serializer = HeavyUserSerializer(user)
        else:
            serializer = LightUserSerializer(user)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        user = self.get_object(pk)
        serializer = HeavyUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        user = self.get_object(pk)
        user.is_active = False
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


########################## MEMBERSHIP #########################################
########################## MEMBERSHIP #########################################
########################## MEMBERSHIP #########################################


class MembershipList(APIView):
    """
    List all users with their status, or attribuate a status to a user.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
        IsActionAllowed,
    ]

    def get(self, request, format=None):

        membership = Membership.objects.all()
        # en fonction du status du user on utilisera Light ou Heavy

        serializer = MembershipSerializer(membership, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        serializer = CreateMembershipSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipDetail(APIView):
    """
    Retrieve or delete an attribution of a user's status.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
        IsActionAllowed,
    ]

    def get_object(self, pk):

        try:
            return Membership.objects.get(id=pk)
        except Membership.DoesNotExist:
            raise Http404


    def delete(self, request, pk, format=None):

        membership = self.get_object(pk)
        membership.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
