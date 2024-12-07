from django.urls import path, include
from . import views
from relationship_app.views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import LogoutView
from relationship_app.views import AdminView, LibrarianView, MemberView


urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/', views.LibraryDetailView.as_view(template_name = 'relationship_app/library_detail.html'), name='library'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.htm'), name='logout'),
    path('login/', LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('register/',views.register.as_view() , name='register'),
 
    path('admin/', AdminView.as_view(), name='admin_view'),
    path('librarian/', LibrarianView, name='librarian_view'),
    path('member/', MemberView, name='member_view'),
]
