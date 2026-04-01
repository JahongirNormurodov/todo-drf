from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.sub_todos.models import SubTodo
from apps.sub_todos.serializers import SubTodoSerializer


class SubTodoViewSet(ModelViewSet):
    serializer_class = SubTodoSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title"]
    ordering_fields = ["position", "created_at", "updated_at"]

    def get_queryset(self):
        queryset = SubTodo.objects.filter(todo__user=self.request.user)
        todo_pk = self.kwargs.get("todo_pk")
        if todo_pk:
            queryset = queryset.filter(todo_id=todo_pk)
        return queryset.order_by("position", "created_at")

    def perform_create(self, serializer):
        todo_pk = self.kwargs.get("todo_pk")
        if todo_pk:
            serializer.save(todo_id=todo_pk)
            return
        serializer.save()
