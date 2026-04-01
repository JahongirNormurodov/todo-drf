from django.contrib.auth import get_user_model
from django.db import models

from apps.common.models import TimeStampedModel

User = get_user_model()


class Label(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="labels")
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#EC4899")

    class Meta:
        ordering = ["title"]
        unique_together = ("user", "title")

    def __str__(self):
        return self.title
