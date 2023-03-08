from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ..models import Membership
from ..serializers import MembershipSerializer, CreateMembershipSerializer
from ..permissions import IsActive, IsNotClient,  IsBoss



class MembershipList(APIView):
    """
    List all users with their status, or attribuate a status to a user.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
        IsBoss,
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
