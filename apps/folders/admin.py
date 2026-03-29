from django.contrib import admin
from .models import  Category
from .models import Folder


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "created_at")

admin.site.register(Category)
