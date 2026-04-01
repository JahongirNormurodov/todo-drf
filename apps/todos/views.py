from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.todos.filters import TodoFilter
from apps.todos.models import Todo
from apps.todos.serializers import TodoDetailSerializer, TodoListSerializer


class TodoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filterset_class = TodoFilter
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at", "due_date", "priority"]

    def get_queryset(self):
        queryset = (
            Todo.objects.filter(user=self.request.user)
            .select_related("folder", "category", "label")
            .prefetch_related("tags", "sub_todos")
        )
        category_pk = self.kwargs.get("category_pk")
        if category_pk:
            queryset = queryset.filter(category_id=category_pk)
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return TodoListSerializer
        return TodoDetailSerializer

    def perform_create(self, serializer):
        category_pk = self.kwargs.get("category_pk")
        if category_pk:
            serializer.save(user=self.request.user, category_id=category_pk)
            return
        serializer.save(user=self.request.user)
