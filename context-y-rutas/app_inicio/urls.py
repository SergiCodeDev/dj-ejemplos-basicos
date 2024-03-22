# URLS.PY NO VIENE POR DEFECTO AL CREAR LA APP

# IMPORTAR MODULOS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pruebavista, name='inicio app_inicio'),
    path('dart/', views.dart, name='dart 2'),
    # para que cuando entremos a un enlace nos ponga la url que pusimos (nombre final) /nombre
    # path('<str:nombre>/', views.saludar, name='saludara'),
    path('moneda/', views.moneda, name="moneda"),
]