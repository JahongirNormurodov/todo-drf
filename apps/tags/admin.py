from django.contrib import admin

from apps.tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "color", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name", "user__username")
