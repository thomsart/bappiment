from rest_framework import permissions



class IsAdmin(permissions.BasePermission):
    """
    Custom permission to allow only owner of an objet to view and edit it
    """
    def has_permission(self, request, view):
        return request.user.profile.role == "1" or request.user.is_superuser


class IsAdminOwner(permissions.BasePermission):
    """
    Custom permission to allow only owner of an objet to view and edit it
    """
    def has_permission(self, request, view):
        return request.user.profile.role == "1" or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.company == request.user.profile.company and request.user.profile.role == "1"


class IsManagerAdminOwner(permissions.BasePermission):
    """
    Custom permission to allow only owner of an objet to view and edit it
    """
    def has_permission(self, request, view):
        return request.user.profile.role in ["1", "2"] or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.company == request.user.profile.company and request.user.profile.role in ["1", "2"]


class IsManagerAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.profile.role in ["1", "2"] or request.user.is_superuser:
            return True
        else:
            return False


class IsTrainerManagerAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.profile.role in ["1", "2", "4"] or request.user.is_superuser


class IsRegieManagerAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.profile.role in ["1", "2", "3"] or request.user.is_superuser:
            return True
        else:
            return False
