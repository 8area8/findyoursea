"""Be sure django works."""

from django.test import Client


client = Client()


def test_home():
    """Django should not crash.

    Its first page is not used - this is an API.
    """
    assert client.get("/").status_code == 404
