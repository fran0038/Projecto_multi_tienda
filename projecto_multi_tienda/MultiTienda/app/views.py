from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app import models
from app.models import Productos, Categorias
from app.bolsaCompra import Bolsa
from django.contrib import messages
from app import formularios
from django.db.models import Q

# Create your views here.

def inicio(request):

     return render(request,'home.html')

def productos(request):
    productos = Productos.objects.all()
    categorias = Categorias.objects.all()
    
    if request.method == 'POST':
        if request.POST['nombreProducto']:
            nombre = request.POST['nombreProducto']
            precio = request.POST['precio']
            detalle = request.POST['detalle']
            imagen = request.POST['imagenes']
            categori = request.POST['tipoCategoria']
            pro = categoria.objects.get(id=categori)
        
            producto = Productos(nombre=nombreProducto, precio=precio, detalle=detalle, categorias=categori,imagenes=imagen)
            producto.save()

    return  render(request, 'ropa.html', {'productos': productos ,'categorias':categorias})

def categoria(request):
    if request.method == 'POST':
        if request.POST['tipoCategoria'] != '':
            pro = request.POST['tipoCategoria']
            categori = Categorias(nombre=pro)
            categori.save()
    return render(request, 'tipoCategoria.html')

def bolsaCompra(request):
        productos = Productos.objects.all()

        return render(request, 'bolsaCompra.html', {'productos': productos})

def agregar_bolsa(request, producto_id):
    bolsita = Bolsa(request)
    producto = Productos.objects.get(id=producto_id)
    bolsita.agregarCompra(producto)
    return redirect("Bolsa")  

def eliminar_producto(request, producto_id):
    bolsita = Bolsa(request)
    producto = Productos.objects.get(id=producto_id)
    bolsita.eliminarCompra(producto)
    return redirect("Bolsa")

def restar_compra(request, producto_id):
    bolsita = Bolsa(request)
    producto = Productos.objects.get(id=producto_id)
    bolsita.resta(producto)
    return redirect("Bolsa")

def limpiar_bolsa(request):
    bolsita = Bolsa(request)
    bolsita.limpiarBolsa()
    return redirect("bolsa")



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

def total_bolsita(request):
    total = 0
    if request.user.is_authenticated:
        if "bolsita" in request.session.keys():
            
            for key , value in request.session["bolsita"].items():
                total += int(value["precio"])
    return {"total_bolsita":total}



