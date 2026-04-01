from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name"]
    ordering_fields = ["position", "created_at", "updated_at"]

    def get_queryset(self):
        queryset = Category.objects.filter(user=self.request.user)
        folder_pk = self.kwargs.get("folder_pk")
        if folder_pk:
            queryset = queryset.filter(folder_id=folder_pk)
        return queryset.order_by("position", "created_at")

    def perform_create(self, serializer):
        folder_pk = self.kwargs.get("folder_pk")
        if folder_pk:
            serializer.save(user=self.request.user, folder_id=folder_pk)
            return
        serializer.save(user=self.request.user)
