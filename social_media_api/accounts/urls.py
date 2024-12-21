from django.urls import path, include
from .views import RegisterView, LoginView, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]