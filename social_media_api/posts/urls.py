from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]