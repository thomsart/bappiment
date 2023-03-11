from rest_framework import permissions

from .models import Status, User, Membership
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

        if Membership.objects.filter(user=request.user.id, status=boss.pk).exists() \
        or request.user.is_superuser:
            return True
        else:
            return False


class IsAccountant(permissions.BasePermission):
    
    def has_permission(self, request, view):

        accountant = Status.objects.get(name=STATUS['accountant'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=accountant.pk).exists()


class IsHr(permissions.BasePermission):
    
    def has_permission(self, request, view):

        hr = Status.objects.get(name=STATUS['hr'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=hr.pk).exists()


class IsCommercial(permissions.BasePermission):
    
    def has_permission(self, request, view):

        commercial = Status.objects.get(name=STATUS['commercial'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=commercial.pk).exists()


class IsRepairOperator(permissions.BasePermission):
    
    def has_permission(self, request, view):

        repair_operator = Status.objects.get(name=STATUS['repair_operator'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=repair_operator.pk).exists()


class IsStockOperator(permissions.BasePermission):
    
    def has_permission(self, request, view):

        stock_operator = Status.objects.get(name=STATUS['stock_operator'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=stock_operator.pk).exists()


class IsReceptionist(permissions.BasePermission):
    
    def has_permission(self, request, view):

        receptionist = Status.objects.get(name=STATUS['receptionist'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=receptionist.pk).exists()


class IsInstaller(permissions.BasePermission):
    
    def has_permission(self, request, view):

        installer = Status.objects.get(name=STATUS['installer'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=installer.pk).exists()


class IsElectrotechnician(permissions.BasePermission):
    
    def has_permission(self, request, view):

        electrotechnician = Status.objects.get(name=STATUS['electrotechnician'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=electrotechnician.pk).exists()


class IsCoppersmith(permissions.BasePermission):
    
    def has_permission(self, request, view):

        coppersmith = Status.objects.get(name=STATUS['coppersmith'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=coppersmith.pk).exists()


class IsLocksmith(permissions.BasePermission):
    
    def has_permission(self, request, view):

        locksmith = Status.objects.get(name=STATUS['locksmith'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=locksmith.pk).exists()


class IsMason(permissions.BasePermission):
    
    def has_permission(self, request, view):

        mason = Status.objects.get(name=STATUS['mason'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=mason.pk).exists()


class IsRepairman(permissions.BasePermission):
    
    def has_permission(self, request, view):

        repairman = Status.objects.get(name=STATUS['repairman'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=repairman.pk).exists()


class IsMaintenanceAgent(permissions.BasePermission):
    
    def has_permission(self, request, view):

        maintenance_agent = Status.objects.get(name=STATUS['maintenance_agent'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=maintenance_agent.pk).exists()


class IsDeliveryman(permissions.BasePermission):

    def has_permission(self, request, view):

        deliveryman = Status.objects.get(name=STATUS['deliveryman'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=deliveryman.pk).exists()






###############################################################################
############################ External user ####################################
###############################################################################


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):

        client = Status.objects.get(name=STATUS['client'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=client.pk).exists()


class IsNotClient(permissions.BasePermission):

    def has_permission(self, request, view):

        client = Status.objects.get(name=STATUS['client'][LANGUAGE])

        return not(Membership.objects.filter(user=request.user.id, status=client.pk).exists())






###############################################################################
############################ object Permissions ###############################
###############################################################################


class IsPostUserAllowed(permissions.BasePermission):
    
    def has_permission(self, request, view):

        boss = Status.objects.get(name=STATUS['boss'][LANGUAGE])

        if request.method == 'POST':
            if Membership.objects.filter(user=request.user.id, status=boss.pk).exists() \
                or request.user.is_superuser:
                    return True
            else:
                return False
        else:
            return True


class IsAcessUserAllowed(permissions.BasePermission):
    """ This permission check for the right to retrieve a user in
    considering the status of the user. """

    def has_object_permission(self, request, view, obj):

        level = request.user.hightest_level

        if int(level) > 1 or request.user.is_superuser:
            return True
        else:
            return False
