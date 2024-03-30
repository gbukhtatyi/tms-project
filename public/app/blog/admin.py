# Django
from django.contrib import admin
# Application
from blog.models import Page, Category, Post


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        "slug",
        "name",
        "content",
        "published_at",
        "created_at",
        "updated_at",
        "allow_comment",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "slug",
        "name",
        "description",
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "slug",
        "name",
        "content",
        "published_at",
        "created_at",
        "updated_at",
        "allow_comment",
    ]
