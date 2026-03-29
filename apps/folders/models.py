
# Create your models here.
import uuid
from django.db import models
from apps.common.models import TimeStampedModel


class Folder(TimeStampedModel):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default="#6366F1")
    icon = models.CharField(max_length=50, default="folder")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "created_at"]

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default="#6366F1")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
