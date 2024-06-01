from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    This is to ensure only the owner can edit/delete the resource
    """
    
    def has_object_permission(self, request, view, obj):
        # if this is read only , let it go
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # otherwise only the owner of the resource can do
        return obj.user == request.user
    