from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
<<<<<<< HEAD
        return request.user == obj.creator or request.user.is_staff
=======
        return request.user == obj.creator or request.user.is_staff
>>>>>>> 3fac880ae731da1208675d2da5b0ea1a741cbb44
