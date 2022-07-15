from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('home', home, name="home"),
    path('login/', login, name="login"),
    path('productos/', productos, name="productos"),
    path('sobrenosotros/', sobrenosotros, name="sobrenosotros"),
    path('despacho/', despacho, name="despacho"),
    path('contactanos/', contactanos, name="contactanos"),
]