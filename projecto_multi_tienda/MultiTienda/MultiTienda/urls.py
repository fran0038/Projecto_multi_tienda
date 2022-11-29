"""MultiTienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from app import formularios
from app.views import bolsaCompra, agregar_bolsa, eliminar_producto, restar_compra, limpiar_bolsa

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', views.inicio, name='home'),
    path('bolsa/', views.bolsaCompra, name='Bolsa'),
    path('ropa/', views.productos, name='ropa'),
    path('login/' , views.Login, name='login'),
    path('formulario/',views.userRegistrationView,name="formulario"),
    path('agregar/<int:producto_id>', agregar_bolsa, name="add"),
    path('eliminar/<int:producto_id>', eliminar_producto, name="delete"),
    path('restar/<int:producto_id>', restar_compra, name="menos"),
    path('limpiar/', limpiar_bolsa, name="limpiar"),

    
]
