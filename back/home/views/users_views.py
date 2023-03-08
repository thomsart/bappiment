from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ..models import User
from ..serializers import LightUserSerializer, HeavyUserSerializer, CreateUserSerializer
from ..permissions import IsActive, IsNotClient,  IsPostUserAllowed, IsGetPutDeleteUserAllowed



class UserList(APIView):
    """
    List all users, or create a new one.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
        IsPostUserAllowed,
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
        IsGetPutDeleteUserAllowed,
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


