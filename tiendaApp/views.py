from django.shortcuts import render

# Create your views here.
from tiendaApp.models import Venta
from tiendaApp.serializers import *
from . import forms
from tiendaApp.forms import FormProducto
from tiendaApp.forms import FormBoleta
from tiendaApp.forms import FormularioUsuario
from django.shortcuts import redirect
from tiendaApp.models import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics


# Create your views here.
def producto(request):
    venta = Venta.objects.all()
    data = {'venta': venta}
    return render(request, 'tiendaApp/productos.html', data)


def RegistrationProducto(request):

    form = FormProducto()
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
        return producto(request)
    data = {'form': form}
    return render(request, 'tiendaApp/RegistrarProducto.html', data)


def eliminar(request, id):
    venta = Venta.objects.get(id=id)
    venta.delete()
    return redirect('/producto')
    # return redirect('/producto')


def actualizar(request, id):
    venta = Venta.objects.get(id=id)
    form = FormProducto(instance=venta)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=venta)
        if form.is_valid():
            form.save()
        return producto(request)

    data = {'form': form}
    return render(request, 'tiendaApp/RegistrarProducto.html', data)


def index(request):
    return render(request, 'tiendaApp/index.html')
# ------- usuario---------


def empleado(request):
    return render(request, "tiendaApp/index.html")


def ListEmpleados(request):
    user = Usuario.objects.all()
    data = {'user': user}
    return render(request, 'tiendaApp/empleados.html', data)


def prosesarFormulario(request):
    form = FormularioUsuario()
    if request.method == 'POST':
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            form.save()
        return empleado(request)
    data = {'form': form}
    return render(request, "tiendaApp/usuarios.html", data)


def eliminar2(request, id):
    user = Usuario.objects.get(id=id)
    user.delete()
    return redirect('../usuarios')


def actualizar2(request, id):
    user = Usuario.objects.get(id=id)
    form = FormularioUsuario(instance=user)
    if request.method == 'POST':
        form = FormularioUsuario(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return empleado(request)
    data = {'form': form}
    return render(request, "tiendaApp/usuarios.html", data)

# ----Boleta--------------


def RegistrarBoleta(request):
    form = FormBoleta()
    if request.method == 'POST':
        form = FormBoleta(request.POST)
        if form.is_valid():
            form.save()
        return listaBoleta(request)
    data = {'form': form}
    return render(request, 'tiendaApp/RegistrarBoleta.html', data)


def listaBoleta(request):
    boleta = Boleta.objects.all()
    data = {'boleta': boleta}
    return render(request, 'tiendaApp/listaBoleta.html', data)


def actualizar3(request, id):
    boleta = Boleta.objects.get(id=id)
    form = FormBoleta(instance=boleta)
    if request.method == 'POST':
        form = FormBoleta(request.POST, instance=boleta)
        if form.is_valid():
            form.save()
        return listaBoleta(request)
    data = {'form': form}
    return render(request, "tiendaApp/RegistrarBoleta.html", data)


def eliminar3(request, id):
    boleta = Boleta.objects.get(id=id)
    boleta.delete()
    return redirect('../listaBoleta')


# --------------------------------------------------------------------------------







##------------------entidades relaciones





class UsuarioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer




class BoletaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class BoletaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer




class VentaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


import requests
import json

def delete_or_update_resource(url, request_type, data=None):
  if request_type == 'DELETE':
    response = requests.delete(url)
  elif request_type == 'PUT':
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, data=json.dumps(data), headers=headers)
  else:
    raise ValueError('Invalid request type')
  
  if response.status_code != 200:
    raise Exception('API request failed')
  
  return response.json()