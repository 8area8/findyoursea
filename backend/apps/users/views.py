"""Basic auth view."""

from rest_framework import mixins
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class Signup(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Create a user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
