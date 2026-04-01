from rest_framework import serializers

from apps.sub_todos.serializers import SubTodoSerializer
from apps.todos.models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    sub_todos_count = serializers.IntegerField(source="sub_todos.count", read_only=True)

    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "status",
            "priority",
            "due_date",
            "folder",
            "category",
            "label",
            "sub_todos_count",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "sub_todos_count"]


class TodoDetailSerializer(serializers.ModelSerializer):
    sub_todos = SubTodoSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "completed_at",
            "folder",
            "category",
            "label",
            "tags",
            "sub_todos",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "sub_todos"]
