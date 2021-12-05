"""User forms."""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class UserAdminForm(UserCreationForm):
    """Admin panel form : no password validations."""

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=_("No password restrictions here. ;)"),
    )

    def _post_clean(self):
        """Hack : avoids validation of UserCreationForm passwords."""
        return forms.ModelForm._post_clean(self)  # type: ignore
