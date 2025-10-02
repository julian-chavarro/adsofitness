from django.contrib import admin
from django.urls import path, include
from . import views  # para la página de inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  # si tienes página de inicio
    path('ejercicios/', include('ejercicios.urls')),
]

