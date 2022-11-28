from django.db import models
from django import forms

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length = 30 ,default='')
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=15,default='')
    




class Ropa(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField()
    precio = models.IntegerField()
    talla = models.IntegerField()
    detalle = models.CharField(max_length=30)


class Electronica(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField()
    precio = models.IntegerField()
    detalle = models.CharField(max_length=30)
    tipo_producto = models.CharField(max_length=30)
    

class Productos(models.Model):
    nombre= models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()


    