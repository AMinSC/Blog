from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=20)
    email = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
