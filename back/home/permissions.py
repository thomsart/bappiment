from rest_framework import permissions

from .models import Status, CustomUser, Membership
from .management.commands.datas import LANGUAGE
from .management.commands.datas.user_status import STATUS



###############################################################################
############################ Internal user ####################################
###############################################################################


class IsActive(permissions.BasePermission):
    """ This permission just check if the user is active. """

    def has_permission(self, request, view):

        return request.user.is_active


class IsPermanentEmployee(permissions.BasePermission):
    """ This permission just check if the user is a permanent employee
    to avoid that an fixed-term contract user messed up in the 
    application. """

    def has_permission(self, request, view):

        return request.user.permanent_contract


class IsBoss(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True

        boss = Status.objects.get(name=STATUS['boss'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=boss.pk).exists()



class IsAccountant(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        accountant = Status.objects.get(name=STATUS['accountant'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=accountant.pk).exists()


class IsHr(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        hr = Status.objects.get(name=STATUS['hr'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=hr.pk).exists()


class IsCommercial(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        commercial = Status.objects.get(name=STATUS['commercial'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=commercial.pk).exists()


class IsTechnicalCommercial(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        teschnical_commercial = Status.objects.get(name=STATUS['teschnical_commercial'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=teschnical_commercial.pk).exists()

class IsRepairOperator(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        repair_operator = Status.objects.get(name=STATUS['repair_operator'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=repair_operator.pk).exists()


class IsStockOperator(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        stock_operator = Status.objects.get(name=STATUS['stock_operator'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=stock_operator.pk).exists()


class IsReceptionist(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        receptionist = Status.objects.get(name=STATUS['receptionist'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=receptionist.pk).exists()


class IsInstaller(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        installer = Status.objects.get(name=STATUS['installer'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=installer.pk).exists()


class IsElectrotechnician(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        electrotechnician = Status.objects.get(name=STATUS['electrotechnician'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=electrotechnician.pk).exists()


class IsCoppersmith(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        coppersmith = Status.objects.get(name=STATUS['coppersmith'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=coppersmith.pk).exists()


class IsLocksmith(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        locksmith = Status.objects.get(name=STATUS['locksmith'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=locksmith.pk).exists()


class IsMason(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        mason = Status.objects.get(name=STATUS['mason'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=mason.pk).exists()


class IsRepairman(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        repairman = Status.objects.get(name=STATUS['repairman'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=repairman.pk).exists()


class IsMaintenanceAgent(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        maintenance_agent = Status.objects.get(name=STATUS['maintenance_agent'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=maintenance_agent.pk).exists()


class IsDeliveryman(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        deliveryman = Status.objects.get(name=STATUS['deliveryman'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=deliveryman.pk).exists()



###############################################################################
############################ External user ####################################
###############################################################################


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.hightest_level == 5:
            return True

        client = Status.objects.get(name=STATUS['client'][LANGUAGE])

        return Membership.objects.filter(user=request.user.id, status=client.pk).exists()


class IsNotClient(permissions.BasePermission):

    def has_permission(self, request, view):

        client = Status.objects.get(name=STATUS['client'][LANGUAGE])

        return not(Membership.objects.filter(user=request.user.id, status=client.pk).exists())



###############################################################################
############################ object Permissions ###############################
###############################################################################


class IsCrudOnUserAllowed(permissions.BasePermission):
    """ This permission check for the right to retrieve a user in
    considering the status of the user. """

    def has_permission(self, request, view):

        level = request.user.hightest_level
        superuser = request.user.is_superuser

        if superuser:
            return True

        if request.method == "GET":
            if int(level) > 1:
                return True

        if request.method in ["POST", "PUT", "DELETE"]:
            if int(level) == 5:
                return True

        return False

    def has_object_permission(self, request, view, obj):

        return not(obj.is_superuser)


class IsCrudOnMembershipAllowed(permissions.BasePermission):
    """ This permission check for the right to retrieve a membership in
    considering the status of the user. """

    def has_permission(self, request, view):

        level = request.user.hightest_level

        if request.user.is_superuser:
            return True

        if request.method == "GET":
            if int(level) > 1:
                return True

        if request.method in ["POST", "DELETE"]:
            if int(level) == 5:
                return True

        return False

    def has_object_permission(self, request, view, obj):

        return True