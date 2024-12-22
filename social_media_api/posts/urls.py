from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedView, LikePostView, UnlikePostView
urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('like/<int:id>', LikePostView.as_view(), name='like'),
    path('unlike/<int:id>', UnlikePostView.as_view(), name='unlike'),
]