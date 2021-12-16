# type: ignore
"""Test the coordinates feature."""

from django.urls import reverse

from backend.apps.coordinates.api import Geocoder

from .fixtures import client

coords_url = reverse("coordinates")


def test_coords_generation():
    """Test the coordinates generation."""
    result = client.get(coords_url)
    assert result.data.get("lat")
    assert result.data.get("long")
    assert isinstance(result.data.get("lat"), float)
    assert isinstance(result.data.get("long"), float)


def test_coords_random():
    """Test the coordinates random generation."""
    result = client.get(coords_url)
    assert result.status_code == 200
    long, lat = result.data.values()
    result = client.get(coords_url)
    assert result.status_code == 200
    long2, lat2 = result.data.values()
    assert (long, lat) != (long2, lat2)


def test_coords_target_sea_only():
    """Check that the coords targets the seas and not the lands."""
    geocoder = Geocoder()
    long, lat = geocoder.generate_sea_coords()
    assert geocoder.is_sea(long, lat)


def test_coords_target_sea_only_from_api():
    """Check that the coords targets the seas and not the lands."""
    result = client.get(coords_url)
    assert result.status_code == 200
    long, lat = result.data.values()
    assert Geocoder().is_sea(long, lat)
