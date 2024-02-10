from rest_framework import permissions

class PostAuthorOrCreateOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS + ('POST',):
            return True
        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user
        
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS + ('POST',) or
            request.user and
            request.user.is_authenticated
        )
    

class CommentAuthor(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class UserAdminOrOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return True
            return obj == request.user
        else:
            return False


class ProfileAdminOrOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return True
            return obj.user == request.user
        else:
            return False