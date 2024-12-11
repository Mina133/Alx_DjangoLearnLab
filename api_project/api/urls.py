from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')
urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),

    path('', include(router.urls)),

    path('api/token/', ObtainAuthToken.as_view(), name='api_token_auth'),
]