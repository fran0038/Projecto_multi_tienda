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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.inicio, name='home'),
    path('bolsa/<int:id>', views.bolsaCompra, name='bolsa'),
    path('ropa/', views.Ropa, name='ropa'),
    path('electronica/', views.Electronica, name='electro'),
    path('jugueteria/', views.Jugueteria, name='juguetes'),
    path('login/' , views.Login, name='login'),
    path('formulario/',views.userRegistrationView,name="formulario"),
    path('menu/', views.Menu)


    
]
