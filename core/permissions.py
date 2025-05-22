from rest_framework import permissions
from django.contrib.auth import authenticate

class AdminPostOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')
            if email and password:
                user = authenticate(request=request, username=email, password=password)
                return user is not None and user.is_staff
            return False
        return True