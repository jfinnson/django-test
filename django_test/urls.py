from django.urls import include, path
from django.contrib import admin

# Urls for happy_team app, api authentication, Django admin, and account management (login, logout, etc)
urlpatterns = [
    path('', include('happy_team.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Account management here for all apps
]
