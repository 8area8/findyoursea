"""Test the coordinates feature."""

from .fixtures import client


def test_coords_generation():
    """Test the coordinates generation."""
    res = client.get("api/coordinates/random/")
    assert res.data.get("lat")
    assert res.data.get("long")
    assert res.data.get("lat").isdigit()
    assert res.data.get("long").isdigit()


def test_coords_random():
    """Test the coordinates random generation."""
    long, lat = client.get("api/coordinates/random/").data.values()
    long2, lat2 = client.get("api/coordinates/random/").data.values()
    assert (long, lat) != (long2, lat2)


def test_coords_target_sea_only():
    """Check that the coords targets the seas and not the lands."""
    geocoder = Geocoder()
    long, lat = geocoder.generate_coords()
    assert geocoder.is_sea(long, lat)


def test_coords_target_sea_only_from_api():
    """Check that the coords targets the seas and not the lands."""
    pass


# from random import uniform
# x, y = uniform(-180,180), uniform(-90, 90)
