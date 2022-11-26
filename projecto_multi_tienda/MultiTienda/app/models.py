from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.IntegerField()




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

