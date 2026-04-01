from django.contrib import admin

from apps.folders.models import Folder


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "position", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name", "user__username")
