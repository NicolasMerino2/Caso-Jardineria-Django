from distutils.command.upload import upload
from hashlib import blake2b
from tabnanny import verbose
from django.db import models

# Create your models here.
class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    Descripcion = models.CharField (max_length=300)
    Tipo = models.CharField (max_length=100)
    def __str__(self):
        return self.nombre

class Macetero(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Macetero')
    precio = models.IntegerField()
    Descripcion = models.CharField (max_length=300)
    Tipo= models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Tierra_de_Hoja(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    Descripcion = models.CharField (max_length=300)
    Abono  = models.CharField (max_length=10)
    
    def __str__(self):
        return self.nombre

class Formulario (models.Model):
    usuario = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)