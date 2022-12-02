from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SimpleViewSet
)

simple_app_router = DefaultRouter()
simple_app_router.register('apps', SimpleViewSet)
