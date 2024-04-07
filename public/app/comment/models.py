# Django
from django.db import models
from django.contrib.auth import get_user_model


class Comment(models.Model):
    # Relations
    type_source = models.CharField(max_length=32, null=False)
    type_id = models.IntegerField(null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, verbose_name="Owner", default=0)
    # Data
    content = models.CharField(max_length=512)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_at']
