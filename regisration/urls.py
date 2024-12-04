from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r"registrations", RegistrationViewSet, basename="registration")

# Include the router's URLs in your urlpatterns
urlpatterns = [
    path("", include(router.urls)),
]
