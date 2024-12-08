from django.urls import path
from . import views
from .views import LogoutView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, CommentUpdateView, CommentDeleteView, PostByTagView
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

     path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

     # Comments
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),


    path('search/', views.PostSearchView.as_view(), name='post-search'),
    path('tags/<slug:tag_slug>/', PostByTagView.as_view(), name='post-by-tag'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

]
