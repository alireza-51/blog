from rest_framework import permissions

class IsAuthorOrCreateOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS + ['POST',]:
            return True
        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user
        
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS + ['POST',] or
            request.user and
            request.user.is_authenticated
        )