"""Note: it's a good practice to override the Abstract user."""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# from django.db import models


class User(AbstractUser):
    """Base user."""

    username = models.CharField(
        "username",
        max_length=150,
        unique=False,
        default="",
        blank=True,
    )
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
