from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OptimizationViewset

router = DefaultRouter()
router.register(r'ml', OptimizationViewset, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]