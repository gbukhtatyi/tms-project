# Django
from django.contrib import admin
# Application
from tag.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["content"]
