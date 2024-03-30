# Django
from django.db import models


class Tag(models.Model):
    content = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.content


class TagTaxomy(models.Model):
    type_source = models.CharField(max_length=32, null=False)
    type_id = models.IntegerField(null=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="Tag")
