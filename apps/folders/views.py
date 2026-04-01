from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.folders.models import Folder
from apps.folders.serializers import FolderSerializer


class FolderViewSet(ModelViewSet):
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name"]
    ordering_fields = ["position", "created_at", "updated_at"]

    def get_queryset(self):
        return Folder.objects.filter(user=self.request.user).order_by("position", "created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
