from django.contrib.auth import get_user_model
from django.db import models

from apps.common.models import TimeStampedModel
from apps.folders.models import Folder

User = get_user_model()


class Category(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        related_name="categories",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default="#16A34A")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "created_at"]
        unique_together = ("user", "name", "folder")

    def __str__(self):
        return self.name
