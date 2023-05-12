from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ..models import Membership, CustomUser, Status
from ..serializers import LightMembershipSerializer, HeavyMembershipSerializer, CreateMembershipSerializer
from ..permissions import IsActive, IsBoss, IsNotClient, IsCrudOnMembershipAllowed



class MembershipList(APIView):
    """
    List all users with their status, or attribute a status to a user .
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsNotClient,
        IsCrudOnMembershipAllowed
    ]

    def get(self, request, format=None):

        membership = Membership.objects.all().prefetch_related('status').prefetch_related('user')

        if int(request.user.hightest_level) >= 4:
            serializer = HeavyMembershipSerializer(membership, many=True)
        else:
            serializer = LightMembershipSerializer(membership, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        serializer = CreateMembershipSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipDetail(APIView):
    """
    Unregister a user from a status.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsCrudOnMembershipAllowed
    ]

    def get_object(self, pk):

        try:
            return Membership.objects.get(id=pk)
        except Membership.DoesNotExist:
            raise Http404


    def delete(self, request, pk, format=None):

        membership = self.get_object(pk)
        other_memberships = Membership.objects.filter(user=membership.user).exclude(id=membership.pk)

        try:
            if len(other_memberships) > 0:
                hightest_level = 0
                user = CustomUser.objects.get(id=membership.user.pk)
                for each_membership in other_memberships:
                    status_obj = Status.objects.get(id=each_membership.status.pk)
                    if int(status_obj.level) > hightest_level:
                        hightest_level = int(status_obj.level)
                membership.delete()
                user.hightest_level = str(hightest_level)
                user.save()

                return Response(status=status.HTTP_204_NO_CONTENT)

            else:
                raise PermissionError

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)
