"""Coordinates views."""

import random

from rest_framework.views import APIView
from rest_framework.response import Response


class CoordinatesView(APIView):
    """Coordinates main view."""

    permission_classes = []

    def get(self, request):
        """Get random coordinates.

        Return data with {'long': int, 'lat': int}
        """
        long, lat = random.uniform(-180, 180), random.uniform(-90, 90)
        return Response(data={"long": long, "lat": lat}, content_type="json")
