"""Coordinates urls."""

from django.urls import path, include

from . import views


urlpatterns = [path("random/", views.CoordinatesView.as_view(), name="coordinates")]
