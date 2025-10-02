from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ejercicios, name='lista_ejercicios'),
    path('crear/', views.crear_ejercicio, name='crear_ejercicio'),
    path('editar/<int:id>/', views.editar_ejercicio, name='editar_ejercicio'),
    path('eliminar/<int:id>/', views.eliminar_ejercicio, name='eliminar_ejercicio'),
]

