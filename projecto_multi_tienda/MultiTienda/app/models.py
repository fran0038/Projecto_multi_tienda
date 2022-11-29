from django.db import models
from django import forms

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length = 30 ,default='')
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=15,default='')
    

class Productos(models.Model):
    imagenes = models.ImageField(upload_to="imagenes")
    nombre= models.CharField(max_length=30)
    precio = models.IntegerField()
    categoria= models.CharField(max_length=30)
    detalle = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    


    