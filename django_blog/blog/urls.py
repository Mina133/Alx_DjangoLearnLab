from django.urls import path
from . import views
from .views import LogoutView
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
