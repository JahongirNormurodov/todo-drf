from django.contrib.auth import get_user_model
from django.db import models

from apps.common.models import TimeStampedModel

User = get_user_model()


class Folder(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folders")
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default="#2563EB")
    icon = models.CharField(max_length=50, default="folder")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "created_at"]
        unique_together = ("user", "name")

    def __str__(self):
        return self.name
