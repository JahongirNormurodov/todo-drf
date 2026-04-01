from django.contrib import admin

from apps.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "folder", "name", "position", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name", "user__username")
