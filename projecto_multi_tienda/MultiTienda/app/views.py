from django.shortcuts import render

from app.models import Productos

# Create your views here.

def inicio(request):
     cant = request.session.get("bolsa_compra", 0)
     bolsa = request.session.get("bolsa", [])

     productos = Productos.objects.all()

     return render(request,'home.html' , {"productos":productos, "bolsa_compra":cant, "bolsa": bolsa})

def bolsaCompra(request, id):
    cantidad = request.session.get("bolsa_compra", 0)
    request.session["bolsa_compra"]= [{id: id , "csntidad": 1}]
    return inicio(request)


def Login(request):
    return render(request, 'login.html')


def Electronica(request):
    return render(request, 'electronica.html')


def Ropa(request):
    return render(request, 'ropa.html')


def Jugueteria(request):
    return render(request, 'jugueteria.html')

def Bolsa(request):
    return render(request, 'bolsaCompra.html')

