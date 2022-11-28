from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from app import models
from django.contrib import messages
from app import formularios
from django.db.models import Q

# Create your views here.

def inicio(request):
     #cant = request.session.get("bolsa_compra", 0)
     #bolsa = request.session.get("bolsa", [])

     #productos = Productos.objects.all()

     return render(request,'home.html')

def bolsaCompra(request, id):
    cantidad = request.session.get("bolsa_compra", 0)
    request.session["bolsa_compra"]= [{id: id , "csntidad": 1}]
    return inicio(request, 'bolsaCompra.html')


def userRegistrationView(request):
    form = formularios.Formulario()
    data = {'form': form }

    usuario = models.Usuario()
    if request.method == 'POST':
        form = formularios.Formulario(request.POST)
        if form.is_valid():
            usuario.nombre = form['nombre'].value()
            usuario.apellido  = form['apellido'].value()
            usuario.telefono = form['telefono'].value()
            usuario.email = form['email'].value()
            usuario.password = form['password'].value()

            usuario.save()
            
        else:
            print("El formulario no es valido")
    else:
        print("El metodo no es POST")
        

    
    return render(request, 'formulario.html', data)





def Login(request):
    
    form2 = formularios.Web()
    context = { 'form2': form2}
    if request.method == 'POST':
        form = formularios.Web(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if models.Usuario.objects.filter(Q(email = email) & Q(password = password)):
                usuarios = models.Usuario.objects.get(Q(email = email)& Q(password = password))

                data = {'usuarios': usuarios}

                return render(request, 'home.html',data)
            else:
                print("no es valido")
        

    else:
        form = UserCreationForm()

    
    return render(request, 'login.html', context)


def Electronica(request):
    return render(request, 'electronica.html')


def Ropa(request):
    return render(request, 'ropa.html')


def Jugueteria(request):
    return render(request, 'jugueteria.html')


def Menu(request):
    return render(request, 'menu.html')


