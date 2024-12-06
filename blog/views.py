from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.

class CustomLoginView(LoginView):
   template_name = 'registration/login.html'
  

class LogoutView(View):
    def post(self, request):
        """Handle POST request to log out the user."""
        logout(request)
        return redirect('login')

    def get(self, request):
        """Render a confirmation page for logout."""
        return render(request, 'registration/logout.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'registration/profile.html', {'form': form})



