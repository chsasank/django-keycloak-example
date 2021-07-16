from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse

from .auth import oauth


def home(request):
    if request.user.is_authenticated:
        user = {
            "username": request.user.username,
            "roles": list(request.user.roles.values_list("name", flat=True)),
            "groups": list(request.user.groups.values_list("name", flat=True)),
        }
    else:
        user = None

    return render(request, "home.html", context={"user": user})


def login_view(request):
    redirect_uri = request.build_absolute_uri(reverse("auth"))
    return oauth.qure.authorize_redirect(request, redirect_uri)


def auth_view(request):
    user = authenticate(request)
    login(request, user)
    return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/")
