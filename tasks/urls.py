# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Ek router banayein aur usmein hamara ViewSet register karein.
router = DefaultRouter()
# YAHAN CHANGE KIYA GAYA HAI
router.register(r'tasks', TaskViewSet, basename='task')

# API URLs ab router dwara automatically generate ho jaayenge.
urlpatterns = [
    path('', include(router.urls)),
]