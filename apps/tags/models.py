from django.contrib.auth import get_user_model
from django.db import models

from apps.common.models import TimeStampedModel

User = get_user_model()


class Tag(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tags")
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#F59E0B")

    class Meta:
        ordering = ["name"]
        unique_together = ("user", "name")

    def __str__(self):
        return self.name
