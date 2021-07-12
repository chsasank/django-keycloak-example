from django.urls import path

from . import views

urlpatterns = [
    path('', views.ExampleView.as_view(), name='index'),
]