from rest_framework import permissions


class IsAuthenticated(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
