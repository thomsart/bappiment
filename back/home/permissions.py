from rest_framework import permissions



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
            return False


class IsPermanentEmployee(permissions.BasePermission):
    """ This permission just check if the user is a permanent employee
    to avoid that an fixed-term contract user messed up in the 
    application. """

    def has_permission(self, request, view):

        if request.user.permanent_contract:
            return True
        else:
            return False


#################################################
#                 Office user                   #
#################################################


class IsBoss(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # if boss or resquest.user.is_superuser:
        return True


class IsAccountant(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsHr(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsCommercial(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsRepairOperator(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsStockOperator(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsReceptionist(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


#################################################
#                On the spot user               #
#################################################


class IsInstaller(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsElectrotechnician(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsCoppersmith(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsLocksmith(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsMason(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsRepairman(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsMaintenanceAgent(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


class IsPostman(permissions.BasePermission):
    
    def has_permission(self, request, view):

        return True


###############################################################################
############################ External user ####################################
###############################################################################


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):

        return True

class IsNotClient(permissions.BasePermission):

    def has_permission(self, request, view):

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
