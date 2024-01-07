from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import MyUserCreationForm, MyAuthenticationForm
from django.contrib import messages


def _login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            redirect('/')
        else:
            raise ObjectDoesNotExist('User not found')
    context = {

    }

    return render(request, 'auth/login.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You should log out")
        return redirect('/')
    form = MyAuthenticationForm()
    if request.method == 'POST':
        form = MyAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Successfully signed in {user.username}')
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'auth/login-form.html', context)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        logout(request)
        messages.error(request, "Logout")
        return redirect('auth:login')
    return render(request, 'auth/logout.html')


def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You should logout first")
        return redirect('/')
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth:login')
    context = {
        "form": form
    }
    return render(request, 'auth/register.html', context)