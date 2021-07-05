from rest_framework.permissions import BasePermission

# FIXME://There is a bug in this


class AdminOnly(BasePermission):
    """ only admin can do this"""

    def has_permission(self, request, obj):
        print(request.user)
        return request.user.is_admin
