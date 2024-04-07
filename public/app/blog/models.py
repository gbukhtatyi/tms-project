# Django
from django.db import models


class Page(models.Model):
    # Data
    slug = models.SlugField()
    name = models.CharField(max_length=64)
    content = models.TextField(max_length=50)
    allow_comment = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    # Data
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    published_at = models.DateTimeField(null=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']


class Post(models.Model):
    # Relations
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Category", null=True)
    # Data
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=64)
    content = models.TextField(max_length=50)
    allow_comment = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
