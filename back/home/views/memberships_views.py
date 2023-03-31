from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ..models import Membership, CustomUser, Status
from ..serializers import MembershipSerializer, CreateMembershipSerializer
from ..permissions import IsActive, IsBoss



class MembershipList(APIView):
    """
    List all users with their status, or attribute a status to a user.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsBoss,
    ]

    def get(self, request, format=None):

        membership = Membership.objects.all().prefetch_related('status').prefetch_related('user')
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
    Delete an attribution of a user's status.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActive,
        IsBoss,
    ]

    def get_object(self, pk):

        try:
            return Membership.objects.get(id=pk)
        except Membership.DoesNotExist:
            raise Http404


    def delete(self, request, pk, format=None):

        membership = self.get_object(pk)
        all_his_status = Membership.objects.filter(user=membership.user).exclude(id=membership.pk)
        if len(all_his_status) > 0:
            user = CustomUser.objects.get(id=membership.user.pk)
            user.hightest_level = str(int(user.hightest_level) - 1)
            for each_membership in all_his_status:
                status_obj = Status.objects.get(id=each_membership.status.pk)
                if int(status_obj.level) > int(user.hightest_level):
                    user.hightest_level = status_obj.level
            membership.delete()
        else:
            raise ValueError(
                'If you want to destitute this user from this status register him in an other before.'
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
