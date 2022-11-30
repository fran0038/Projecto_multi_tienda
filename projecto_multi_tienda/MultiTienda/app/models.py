from django.db import models
from django import forms


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length = 30 ,default='')
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=15,default='')
    
class Categorias(models.Model):
    nombre = models.CharField(max_length=10)



class Productos(models.Model):
    imagenes = models.URLField()
    nombre= models.CharField(max_length=30)
    precio = models.IntegerField()
    talla=models.CharField(max_length=10)
    categorias= models.ForeignKey(Categorias, on_delete=models.CASCADE,null=True, default='')
    detalle = models.CharField(max_length=600)


    def __str__(self):
        return f'{self.nombre} -> {self.precio}'


class Electronica(models.Model):
    imagenes = models.URLField()
    nombre= models.CharField(max_length=30)
    precio = models.IntegerField()
    categorias= models.ForeignKey(Categorias, on_delete=models.CASCADE,null=True, default='')
    detalle = models.CharField(max_length=600)


    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Jugueteria(models.Model):
    imagenes = models.URLField()
    nombre= models.CharField(max_length=30)
    precio = models.IntegerField()
    categorias= models.ForeignKey(Categorias, on_delete=models.CASCADE,null=True, default='')
    detalle = models.CharField(max_length=600)


    def __str__(self):
        return f'{self.nombre} -> {self.precio}'




    