# Django
from django.contrib import admin
# Application
from comment.models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "type_source",
        "type_id",
        "user",
        "content"
    ]
