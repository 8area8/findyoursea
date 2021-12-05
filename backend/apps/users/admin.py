"""Register the user."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserAdminForm


class UserAdminPlus(UserAdmin):
    """User admin."""

    add_form = UserAdminForm


admin.site.register(User, UserAdminPlus)
