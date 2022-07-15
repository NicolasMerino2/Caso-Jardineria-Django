from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto
# Create your views here.

def home(request):

    return render(request, 'crud/home.html')


def sobrenosotros(request):
    return render(request, 'crud/sobrenosotros.html')

def contacto(request):
    return render(request, 'crud/contacto.html')

def login(request):
    return render(request, 'crud/login.html')


def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'crud/productos.html')


def despacho(request):
    return render(request, 'crud/despacho.html')