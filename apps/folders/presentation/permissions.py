from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS → hammaga ruxsat
        if request.method in SAFE_METHODS:
            return True
        
        # POST, PUT, DELETE → faqat admin
        return request.user and request.user.is_staff