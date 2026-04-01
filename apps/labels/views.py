from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.labels.models import Label
from apps.labels.serializers import LabelSerializer


class LabelViewSet(ModelViewSet):
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title"]
    ordering_fields = ["title", "created_at", "updated_at"]

    def get_queryset(self):
        return Label.objects.filter(user=self.request.user).order_by("title")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
