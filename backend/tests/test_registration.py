"""Test the registration."""

from django.test import Client
import pytest

from backend.apps.users.models import User


client = Client()


@pytest.mark.django_db
def test_add_user():
    """Test the basic add of a user."""
    data = {"email": "test@gmail.com", "password": "helloworld123&é"}
    res = client.post("/api/users/signup/", data)
    assert res.status_code == 201
    user = User.objects.all().first()
    assert user is not None
    assert user.email == "test@gmail.com"


@pytest.mark.django_db
def test_unique_email():
    """Check that email is unique."""
    data = {"email": "test@gmail.com", "password": "helloworld123&é"}
    client.post("/api/users/signup/", data)
    res = client.post("/api/users/signup/", data)
    assert res.status_code == 400
    assert "user with this email address already exists." in res.json().get("email", [])
    assert len(User.objects.all()) == 1
