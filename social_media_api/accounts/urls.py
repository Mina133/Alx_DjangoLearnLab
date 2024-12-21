from django.urls import path, include
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]