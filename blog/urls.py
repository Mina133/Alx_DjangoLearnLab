from django.urls import path
from .views import register, profile_view, CustomLoginView, LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
     path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),

]