# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls), #Ruta seccion de admin
    path('usuario/', include('usuario.urls')), #Ruta alimenta urls de usuario
    path('', lambda request: render(request, 'home.html'), name='home'),  # Página principal
]
