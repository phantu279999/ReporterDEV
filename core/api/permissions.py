from rest_framework.permissions import IsAuthenticated


class IsAuthor(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'author'

class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'admin'