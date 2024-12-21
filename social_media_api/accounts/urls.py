from django.urls import path, include
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/follow//<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('users/unfollow//<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]