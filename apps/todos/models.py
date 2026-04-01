from django.contrib.auth import get_user_model
from django.db import models

from apps.categories.models import Category
from apps.common.models import TimeStampedModel
from apps.folders.models import Folder
from apps.labels.models import Label
from apps.tags.models import Tag

User = get_user_model()


class TodoStatus(models.TextChoices):
    TODO = "todo", "Todo"
    IN_PROGRESS = "in_progress", "In Progress"
    DONE = "done", "Done"


class TodoPriority(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"


class Todo(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    folder = models.ForeignKey(
        Folder,
        on_delete=models.SET_NULL,
        related_name="todos",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="todos",
        null=True,
        blank=True,
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.SET_NULL,
        related_name="todos",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=TodoStatus.choices, default=TodoStatus.TODO)
    priority = models.CharField(max_length=20, choices=TodoPriority.choices, default=TodoPriority.MEDIUM)
    due_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="todos", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
