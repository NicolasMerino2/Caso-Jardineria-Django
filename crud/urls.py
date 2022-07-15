from django.urls import path
from .views import home,sobrenosotros,contacto,login,productos,despacho

urlpatterns = [
    path('home/', home , name='home'),
    path('sobrenosotros/', sobrenosotros, name='sobrenosotros'),
    path('contacto/', contacto, name='contacto'),
    path('login/', login, name='login'),
    path('productos/', productos, name='productos'),
    path('despacho/', despacho, name='despacho'),
]