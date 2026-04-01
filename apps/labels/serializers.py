from rest_framework import serializers

from apps.labels.models import Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["id", "title", "color"]
        read_only_fields = ["id"]
