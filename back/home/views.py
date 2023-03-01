from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .models import CustomUser, CustomUserStatus, Membership
from .serializers import LightCustomUserSerializer, HeavyCustomUserSerializer
from .permissions import IsActiveUser, IsPermanentEmployee,\
                         IsBoss, IsAccountant, IsHr, IsCommercial, IsRepairOperator, IsReceptionist, IsStockOperator,\
                         IsInstaller, IsElectrotechnician, IsCoppersmith, IsLocksmith, IsMason, IsRepairman, IsMaintenanceAgent, IsPostman,\
                         IsClient,\
                         IsActionAllowed\



# class LightCustomUserList(APIView):
#     """
#     List all users, or create a new one.
#     """

#     permission_classes = [
#         permissions.IsAuthenticated,
#         IsActiveUser,
#     ]

#     def get(self, request, format=None):

        
#         users = CustomUser.objects.all().order_by('-date_joined')
#         serializer = LightCustomUserSerializer(users, many=True)

#         return Response(serializer.data)


# class LightCustomUserDetail(APIView):
#     """
#     Retrieve, update or delete a user instance.
#     """

#     def get_object(self, pk):

#         try:
#             return CustomUser.objects.get(pk=pk)
#         except CustomUser.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):

#         user = self.get_object(pk)
#         serializer = LightCustomUserSerializer(user)

#         return Response(serializer.data)


##############################################################
##############################################################
##############################################################


class CustomUserList(APIView):
    """
    List all users, or create a new one.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActiveUser,
        IsPermanentEmployee,

        IsBoss,
        IsAccountant,
        IsHr,
        IsCommercial,
        IsRepairOperator,

        IsReceptionist,
        IsStockOperator,
        IsInstaller,
        IsElectrotechnician,
        IsCoppersmith,
        IsLocksmith,
        IsMason,
        IsRepairman,
        IsMaintenanceAgent,
        IsPostman,

        IsActionAllowed,
    ]

    def get(self, request, format=None):

        users = CustomUser.objects.all().order_by('-date_joined')
        serializer = HeavyCustomUserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = HeavyCustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsActiveUser,
        IsPermanentEmployee,

        IsBoss,
        IsAccountant,
        IsHr,
        IsCommercial,
        IsRepairOperator,

        IsReceptionist,
        IsStockOperator,
        IsInstaller,
        IsElectrotechnician,
        IsCoppersmith,
        IsLocksmith,
        IsMason,
        IsRepairman,
        IsMaintenanceAgent,
        IsPostman,

        IsActionAllowed,
    ]

    def get_object(self, pk):

        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        user = self.get_object(pk)
        serializer = HeavyCustomUserSerializer(user)

        return Response(serializer.data)

    def put(self, request, pk, format=None):

        user = self.get_object(pk)
        serializer = HeavyCustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        user = self.get_object(pk)
        user.is_active = False
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)