from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('despacho',views.despacho, name='despacho'),
    path('login',views.login,name='login'),
    path('productos',views.login,name='productos'),
    path('sobrenosotros',views.login,name='sobrenosotros'),
]