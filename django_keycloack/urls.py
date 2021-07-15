from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('qure_keycloak_auth.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
