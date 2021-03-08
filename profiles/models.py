from django.contrib.auth.models import AbstractUser
from django.db import models
from db.models import BaseModel


class User(AbstractUser, BaseModel):

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        default=None,
        null=True
    )