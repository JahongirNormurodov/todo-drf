from rest_framework import serializers

from apps.categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "folder", "name", "color", "position", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
