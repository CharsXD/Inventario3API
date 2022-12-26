"""Inventario2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tiendaApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/',producto),
    path('Registrar/',RegistrationProducto),
    path('eliminar/<int:id>',eliminar),
    path('actualizar/<int:id>',actualizar),
    path('',index),
    #usuario
    path('empleados/', prosesarFormulario),
    path('usuarios/', ListEmpleados),
    path('eliminar2/<int:id>', eliminar2),
    path('actualizar2/<int:id>', actualizar2),
    #boleta
    path('listaBoleta/',listaBoleta),
    path('RegistrarBoleta/',RegistrarBoleta),
    path('eliminar3/<int:id>', eliminar3),
    path('actualizar3/<int:id>', actualizar3),
    #cccc
    path('listaUSUARIO/', UsuarioListCreateAPIView.as_view(), name='lista_usuarios'),
    path('listaBoleta/', BoletaListCreateAPIView.as_view(), name='lista_Boleta'),
    path('listaVenta/', VentaListCreateAPIView.as_view(), name='lista_Venta'),



]
