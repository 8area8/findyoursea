"""Note: it's a good practice to override the Abstract user."""

from django.contrib.auth.models import AbstractUser

# from django.db import models


class User(AbstractUser):
    """Base user."""
