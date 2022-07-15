from mailbox import NoSuchMailboxError
from django.db import models
from django.forms import ModelChoiceField

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre
