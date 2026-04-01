from rest_framework import serializers

from apps.folders.models import Folder


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ["id", "name", "color", "icon", "position", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
