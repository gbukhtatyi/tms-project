# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_subscribed = models.BooleanField(default=0)

    class Meta:
        db_table = "users"
