from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('auth/', views.auth_view, name='auth'),
]
