"""Coordinates views."""

import random

from rest_framework.views import APIView
from rest_framework.response import Response

from backend.apps.coordinates.api import Geocoder


class CoordinatesView(APIView):
    """Coordinates main view."""

    permission_classes = []

    def get(self, request):
        """Get random coordinates.

        Return data with {'long': int, 'lat': int}
        """
        geocoder = Geocoder()
        long, lat = geocoder.generate_sea_coords()
        return Response(data={"long": long, "lat": lat}, content_type="json")
