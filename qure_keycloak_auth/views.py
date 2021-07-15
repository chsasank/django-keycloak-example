import json
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .auth import oauth


def home(request):
    if request.user.is_authenticated:
        user = {'userid': request.user.id}
    else:
        user = None

    return render(request, 'home.html', context={'user': user})


def login_view(request):
    redirect_uri = request.build_absolute_uri(reverse('auth'))
    return oauth.qure.authorize_redirect(request, redirect_uri)


def auth_view(request):
    user = authenticate(request)
    login(request, user)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')
