from rest_framework.permissions import BasePermission

# FIXME://There is a bug in this


class AdminOnly(BasePermission):
    """ only admin can do this"""

    def has_permission(self, request, obj):
        return request.user.is_admin


class AgentOnly(BasePermission):
    """ permission for agents"""

    def has_permission(self, request, view):
        return request.user.role == 'AGENT'
