from django.db import models

from apps.common.models import TimeStampedModel
from apps.todos.models import Todo


class SubTodo(TimeStampedModel):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="sub_todos")
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "created_at"]

    def __str__(self):
        return self.title
