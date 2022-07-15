from django.shortcuts import render, redirect
from django.http import HttpResponse 

# Create your views here.

def root(request):

    return redirect('/home')

def home(request):

    return render(request, 'core/home.html')

def login(request):

    return render(request, 'core/login.html')

def productos(request):
    
    return render(request, 'core/productos.html')

def sobrenosotros(request):
    
    return render(request, 'core/sobrenosotros.html')

def despacho(request):
    
    return render(request, 'core/despacho.html')    

def contactanos(request):
    
    return render(request, 'core/contactanos.html')