from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PropertyViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls

