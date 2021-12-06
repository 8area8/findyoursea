"""User serializers."""

from django.core import exceptions
import django.contrib.auth.password_validation as validators
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Basic user serializer."""

    class Meta:
        """Meta."""

        model = User
        fields = ["id", "email", "password"]

    def validate_password(self, value):
        """Use password validation."""
        try:
            validators.validate_password(password=value)
        except exceptions.ValidationError as error:
            raise serializers.ValidationError(str(error))
        return value

    def create(self, validated_data):
        """Use make_password."""
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(UserSerializer, self).create(validated_data)
