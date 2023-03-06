from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from .models import User, Status, Membership

###############################################################################
############################ Internal user ####################################
###############################################################################


class IsActive(permissions.BasePermission):
    """ This permission just check if the user is a permanent employee
    to avoid that an fixed-term contract user messed up in the 
    application. """

    def has_permission(self, request, view):

        if request.user.is_active:
            return True
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "You are deactivate"})


class IsPermanentEmployee(permissions.BasePermission):
    """ This permission just check if the user is a permanent employee
    to avoid that an fixed-term contract user messed up in the 
    application. """

    def has_permission(self, request, view):

        if request.user.permanent_contract:
            return True
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "You are not permanent employee"})


#################################################
#                 Office user                   #
#################################################


class IsBoss(permissions.BasePermission):

    def has_permission(self, request, view):
        
        boss_status = Status.objects.get(name="boss")
        if Membership.objects.get(user=request.user.id, status=boss_status.id) or request.user.is_superuser:
            return True
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "Your are not the Boss"})

class IsAccountant(permissions.BasePermission):
    
    def has_permission(self, request, view):

        accountant_status = Status.objects.get(name="accountant")
        if Membership.objects.get(user=request.user.id, status=accountant_status.id):
            return True
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "You are not an Accountant"})


class IsHr(permissions.BasePermission):
    
    def has_permission(self, request, view):

        hr_status = Status.objects.get(name="hr")
        if Membership.objects.get(user=request.user.id, status=hr_status.id):
            return True
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "you are  not a Hr"})


class IsCommercial(permissions.BasePermission):
    
    def has_permission(self, request, view):

        commercial_status = Status.objects.get(name="commercial")
        if Membership.objects.get(user=request.user.id, status=commercial_status.id):
            return True
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "You are not a Commercial"})


class IsRepairOperator(permissions.BasePermission):
    
    def has_permission(self, request, view):

        repair_operator_status = Status.objects.get(name="repair_operator")
        if Membership.objects.get(user=request.user.id, status=repair_operator_status.id):
            return True
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "You are not a Repair Operator"})


class IsStockOperator(permissions.BasePermission):
    
    def has_permission(self, request, view):

        stock_operator_status = Status.objects.get(name="stock_operator")
        if Membership.objects.get(user=request.user.id, status=stock_operator_status.id):
            return True
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "You are not a Stock Operator"})


class IsReceptionist(permissions.BasePermission):
    
    def has_permission(self, request, view):

        receptionist_status = Status.objects.get(name="receptionist")
        if Membership.objects.get(user=request.user.id, status=receptionist_status.id):
            return True
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"detail": "You are not a Receptionist"})


#################################################
#                On the spot user               #
#################################################


class IsInstaller(permissions.BasePermission):
    
    def has_permission(self, request, view):

        installer_status = Status.objects.get(name="installer")
        if Membership.objects.get(user=request.user.id, status=installer_status.id):
            return True
        else:
            return False


class IsElectrotechnician(permissions.BasePermission):
    
    def has_permission(self, request, view):

        electrotechnician_status = Status.objects.get(name="electrotechnician")
        if Membership.objects.get(user=request.user.id, status=electrotechnician_status.id):
            return True
        else:
            return False


class IsCoppersmith(permissions.BasePermission):
    
    def has_permission(self, request, view):

        coppersmith_status = Status.objects.get(name="coppersmith")
        if Membership.objects.get(user=request.user.id, status=coppersmith_status.id):
            return True
        else:
            return False


class IsLocksmith(permissions.BasePermission):
    
    def has_permission(self, request, view):

        locksmith_status = Status.objects.get(name="locksmith")
        if Membership.objects.get(user=request.user.id, status=locksmith_status.id):
            return True
        else:
            return False


class IsMason(permissions.BasePermission):
    
    def has_permission(self, request, view):

        mason_status = Status.objects.get(name="mason")
        if Membership.objects.get(user=request.user.id, status=mason_status.id):
            return True
        else:
            return False


class IsRepairman(permissions.BasePermission):
    
    def has_permission(self, request, view):

        repairman_status = Status.objects.get(name="repairman")
        if Membership.objects.get(user=request.user.id, status=repairman_status.id):
            return True
        else:
            return False


class IsMaintenanceAgent(permissions.BasePermission):
    
    def has_permission(self, request, view):

        maintenance_agent_status = Status.objects.get(name="maintenance_agent")
        if Membership.objects.get(user=request.user.id, status=maintenance_agent_status.id):
            return True
        else:
            return False


class IsPostman(permissions.BasePermission):
    
    def has_permission(self, request, view):

        postman_status = Status.objects.get(name="postman")
        if Membership.objects.get(user=request.user.id, status=postman_status.id):
            return True
        else:
            return False


###############################################################################
############################ External user ####################################
###############################################################################


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):

        client_status = Status.objects.get(name="client")
        try:
            Membership.objects.get(user_id=request.user.id, status_id=client_status.id)
            return True

        except Membership.DoesNotExist:
            return False

class IsNotClient(permissions.BasePermission):

    def has_permission(self, request, view):

        client_status = Status.objects.get(name="client")
        try:
            Membership.objects.get(user_id=request.user.id, status_id=client_status.id)
            return False

        except Membership.DoesNotExist:
            return True


###############################################################################
############################ object Permissions ###############################
###############################################################################


class IsActionAllowed(permissions.BasePermission):
    """ This permission check for the post, put and delete actions if the 
    user is allowed to process it in considering his status and the concerned 
    datas. """

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser or request.user.status == 'boss' or request.method == 'GET':
            return True

        elif request.method == 'PUT' and request.user.status == "accountant":
            return True

        else:
            return  False
