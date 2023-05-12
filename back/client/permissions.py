from rest_framework import permissions

from .models import LegalEntity, Client, Installation
from home.models import Status, Membership
from home.management.commands.datas import LANGUAGE
from home.management.commands.datas.user_status import STATUS
from home.permissions import IsBoss



###############################################################################
############################ object Permissions ###############################
###############################################################################


class IsCrudOnClientAllowed(permissions.BasePermission):
    """ This permission check for the right to perform CRUD on a client in
    considering the status of the user. """

    def has_permission(self, request, view):

        level = request.user.hightest_level
        superuser = request.user.is_superuser
        commercial = Status.objects.get(name=STATUS['commercial'][LANGUAGE])
        technical_commercial = Status.objects.get(name=STATUS['technical_commercial'][LANGUAGE])
        allowed_status = Membership.objects.filter(
            user=request.user.id,
            status_has_any_keys=[commercial.pk, technical_commercial.pk]
        ).exists()

        if superuser or level == 5:
            return True

        if request.method == "GET":
            if int(level) > 2:
                return True

        if request.method == 'POST':
            if allowed_status:
                return True

        if request.method == "PUT":
            if int(level) > 3:
                return True

        if request.method == "DELETE":
            if int(level) == 5:
                return True

        return False

    def has_object_permission(self, request, view, obj):

        return obj.is_still_client
