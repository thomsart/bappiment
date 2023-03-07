from rest_framework import permissions

from .models import Status, Membership
from .db import LANGUAGE
from .db.datas.user_status import STATUS



###############################################################################
############################ Internal user ####################################
###############################################################################


class IsActive(permissions.BasePermission):
    """ This permission just check if the user is active. """

    def has_permission(self, request, view):

        if request.user.is_active == True:
            return True
        else:
            return False


class IsPermanentEmployee(permissions.BasePermission):
    """ This permission just check if the user is a permanent employee
    to avoid that an fixed-term contract user messed up in the 
    application. """

    def has_permission(self, request, view):

        if request.user.permanent_contract == True:
            return True
        else:
            return False


class IsBoss(permissions.BasePermission):

    def has_permission(self, request, view):

        boss = Status.objects.get(name=STATUS['boss'][LANGUAGE])

        if Membership.objects.exists(user=request.user.id, status=boss.pk) \
        or request.user.is_superuser:
            return True
        else:
            return False

class IsAccountant(permissions.BasePermission):
    
    def has_permission(self, request, view):

        accountant = Status.objects.get(name=STATUS['accountant'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=accountant.pk)


class IsHr(permissions.BasePermission):
    
    def has_permission(self, request, view):

        hr = Status.objects.get(name=STATUS['hr'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=hr.pk)


class IsCommercial(permissions.BasePermission):
    
    def has_permission(self, request, view):

        commercial = Status.objects.get(name=STATUS['commercial'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=commercial.pk)


class IsRepairOperator(permissions.BasePermission):
    
    def has_permission(self, request, view):

        repair_operator = Status.objects.get(name=STATUS['repair_operator'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=repair_operator.pk)


class IsStockOperator(permissions.BasePermission):
    
    def has_permission(self, request, view):

        stock_operator = Status.objects.get(name=STATUS['stock_operator'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=stock_operator.pk)


class IsReceptionist(permissions.BasePermission):
    
    def has_permission(self, request, view):

        receptionist = Status.objects.get(name=STATUS['receptionist'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=receptionist.pk)


class IsInstaller(permissions.BasePermission):
    
    def has_permission(self, request, view):

        installer = Status.objects.get(name=STATUS['installer'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=installer.pk)


class IsElectrotechnician(permissions.BasePermission):
    
    def has_permission(self, request, view):

        electrotechnician = Status.objects.get(name=STATUS['electrotechnician'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=electrotechnician.pk)


class IsCoppersmith(permissions.BasePermission):
    
    def has_permission(self, request, view):

        coppersmith = Status.objects.get(name=STATUS['coppersmith'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=coppersmith.pk)


class IsLocksmith(permissions.BasePermission):
    
    def has_permission(self, request, view):

        locksmith = Status.objects.get(name=STATUS['locksmith'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=locksmith.pk)


class IsMason(permissions.BasePermission):
    
    def has_permission(self, request, view):

        mason = Status.objects.get(name=STATUS['mason'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=mason.pk)


class IsRepairman(permissions.BasePermission):
    
    def has_permission(self, request, view):

        repairman = Status.objects.get(name=STATUS['repairman'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=repairman.pk)


class IsMaintenanceAgent(permissions.BasePermission):
    
    def has_permission(self, request, view):

        maintenance_agent = Status.objects.get(name=STATUS['maintenance_agent'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=maintenance_agent.pk)


class IsDeliveryman(permissions.BasePermission):

    def has_permission(self, request, view):

        deliveryman = Status.objects.get(name=STATUS['deliveryman'][LANGUAGE])

        return Membership.objects.exists(user=request.user.id, status=deliveryman.pk)


###############################################################################
############################ External user ####################################
###############################################################################


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):

        client = Status.objects.get(name=STATUS['client'][LANGUAGE])

        return Membership.objects.exists(user_id=request.user.id, status_id=client.pk)


class IsNotClient(permissions.BasePermission):

    def has_permission(self, request, view):

        client = Status.objects.get(name=STATUS['client'][LANGUAGE])

        return not(Membership.objects.exists(user=request.user.id, status=client.pk))


###############################################################################
############################ object Permissions ###############################
###############################################################################


class IsActionAllowed(permissions.BasePermission):
    """ This permission check for the post, put and delete actions if the 
    user is allowed to process it in considering his status and the concerned 
    datas. """

    def has_object_permission(self, request, view, obj):

        boss = Status.objects.get(name=STATUS['boss'][LANGUAGE])
        accountant = Status.objects.get(name=STATUS['accountant'][LANGUAGE])

        if request.user.is_superuser \
            or Membership.objects.exists(user=request.user.id, status=boss.pk) \
            or request.method == 'GET':
            return True

        elif request.method == 'PUT' \
            and Membership.objects.exists(user=request.user.id, status=accountant.pk):
            return True

        else:
            return False
