from django.shortcuts import render
from .models import Book
from .models import Library
from bookshelf.models import Book
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LogoutView
from django.views import View

from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
    
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get(self, request):
        libList = Library.objects.all()
        library = Library.objects.get(pk = libList.first().pk)
        return render(request, self.template_name, {'library': library})

class register(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class LoginView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('books')



class LogoutView(View):
    template_name = 'registration/logout.html'
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
    
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/logout.html')
    


from .models import UserProfile

# Utility function to check user role
def is_user_role(user, role):
    """
    Checks if a user has a specific role.

    Args:
        user: The user object.
        role: The role to check.

    Returns:
        True if the user has the specified role, False otherwise.
    """
    if not user.is_authenticated:
        return False  # User must be authenticated

    # Check if the user has a profile and the role
    profile = getattr(user, 'profile', None)
    if profile is None:
        print(f"User {user.username} has no profile.")
        return False
    return profile.role == role


# Specific role-checking methods
def is_admin(user):
    return is_user_role(user, 'Admin')


def is_librarian(user):
    return is_user_role(user, 'Librarian')


def is_member(user):
    return is_user_role(user, 'Member')
# Admin view


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_admin), name='dispatch')
class AdminView(View):
    def get(self, request):
        return render(request, 'accounts/admin_view.html', {'message': 'Welcome, Admin!'})
    
@login_required
@user_passes_test(is_librarian)
class LibrarianView(View):
    def get(self, request):
        return render(request, 'accounts/librarian_view.html')


@login_required
@user_passes_test(is_member)
class MemberView(View):
    def get(self, request):
        return render(request, 'accounts/member_view.html')
