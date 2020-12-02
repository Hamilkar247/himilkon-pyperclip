from rest_framework import permissions

#https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#updating-our-serializer
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        #Read permission are allowed to any request
        #so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user