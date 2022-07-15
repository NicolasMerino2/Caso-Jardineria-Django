from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'crud/index.html')

def despacho(request):
    return render(request, 'crud/despacho.html')

def login(request):
    return render(request, 'crud/login.html')


def productos(request):
    return render(request, 'crud/productos.html')


def sobrenosotros(request):
    return render(request, 'crud/sobrenosotros.html')