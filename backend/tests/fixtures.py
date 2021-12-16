"""Pytest fixtures."""

from rest_framework.test import APIClient
import pytest

from dotenv import load_dotenv

from backend.apps.users.models import User


load_dotenv()
client = APIClient()


@pytest.mark.django_db
@pytest.fixture
def user():
    """Create a user."""
    data = {"email": "test@gmail.com", "password": "mypassword123&é"}
    res = client.post("/api/users/signup/", data)
    assert res.status_code == 201
