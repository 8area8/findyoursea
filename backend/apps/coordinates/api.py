"""API coords."""

import os
import random
from typing import Tuple

import requests


class OnWaterAPI:
    """On Water API wrapper.

    url: https://onwater.io/
    """

    def is_sea(self, long: float, lat: float) -> bool:
        """Return true if long,lat targets a sea."""
        url = f"https://api.onwater.io/api/v1/results/{long},{lat}"
        response = requests.get(
            url, params={"access_token": os.getenv("ONWATER_API_KEY", "")}
        )
        if response.status_code != 200:
            return False  # set a logger ?

        data = response.json()
        return data.get("water", False)


class Geocoder:
    """Coords utilities."""

    api = OnWaterAPI()

    def is_sea(self, lat: float, long: float) -> bool:
        """Return True if the lat,long targets the sea."""
        return self.api.is_sea(lat, long)

    def _generate_coords(self) -> Tuple[float, float]:
        """Generate random coordinates."""
        return random.uniform(-180, 180), random.uniform(-90, 90)

    def generate_sea_coords(self):
        """Generate some sea coordinates.

        NOTE for later: find a better way to find the sea coordinates.
        """
        long, lat = -9999.100, -9999.100
        while not self.is_sea(long, lat):
            long, lat = self._generate_coords()

        return long, lat
