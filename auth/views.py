from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .form import MyUserCreationForm, MyAuthenticationForm


def _login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username)
        # print(password)
        user = authenticate(request, username=username, password=password)
        if not user:
            raise ObjectDoesNotExist("user not found, username or password is incorrect")

        login(request, user)
        return redirect('/')
    context = {
    }
    return render(request, 'auth/login.html', context=context)


def login_view(request):
    form = MyAuthenticationForm()
    if request.method == 'POST':
        form = MyAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Successfully signed in {user.username}')
            return redirect('/')

    context = {
            "form": form
    }
    return render(request, 'auth/login_form.html',context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.error(request, 'Successfully logged out {user.username}')
        return redirect('auth:login')
    return render(request, 'auth/logout.html')


def register_view(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth:login')
    context = {
        "form": form,
    }
    return render(request, 'auth/register.html', context)