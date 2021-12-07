"""Test the connection"""

from unittest.mock import patch

import pytest
from rest_framework import permissions

from backend.apps.users.views import Signup
from .fixtures import user, client


@pytest.mark.django_db
def test_basic_login(user):
    """Test a basic login."""
    data = {"email": "test@gmail.com", "password": "mypassword123&é"}
    res = client.post("/api/token/", data, format="json")
    assert res.status_code == 200


@pytest.mark.django_db
def test_wrong_login(user):
    """Test a basic login."""
    # wrong password :
    data = {"email": "test@gmail.com", "password": "wrong password"}
    res = client.post("/api/token/", data, format="json")
    assert res.status_code == 401
    # wrong email :
    data = {"email": "wrong email", "password": "mypassword123&é"}
    res = client.post("/api/token/", data, format="json")
    assert res.status_code == 401


@pytest.mark.django_db
def test_jwt_permissions(user):
    """Check the JWT permissions."""
    with patch(
        "backend.apps.users.views.Signup.permission_classes",
        [permissions.IsAuthenticated],
    ):
        data = {"email": "test_foo@gmail.com", "password": "mypassword123&é"}
        locked_res = client.post("/api/users/signup/", data)
        assert locked_res.status_code == 401

        login_data = {"email": "test@gmail.com", "password": "mypassword123&é"}
        res = client.post("/api/token/", login_data, format="json")
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {res.data['access']}")

        locked_res = client.post("/api/users/signup/", data)
        assert locked_res.status_code == 201
