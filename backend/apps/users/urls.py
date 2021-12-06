"""Users urls."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views


router = DefaultRouter()
router.register("signup", views.Signup, basename="signup")

router_read = DefaultRouter()


urlpatterns = [path("", include(router.urls)), path("", include(router_read.urls))]
