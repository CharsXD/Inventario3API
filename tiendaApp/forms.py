from django import forms
from django.core import validators
from tiendaApp.models import Venta
from tiendaApp.models import Usuario
from tiendaApp.models import Boleta

class RegistroProducto(forms.Form):
    ESTADOS =[('activo','ACTIVO'),('inactivo','INACTIVO')]
    Cventa = forms.CharField()
    Cproductos= forms.CharField(validators=[ #aqui tengo un validator
        validators.MinLengthValidator(2),
        validators.MaxLengthValidator(30)
    ])
    Descripcion = forms.CharField()
    Cantidad = forms.CharField()
    Categoria = forms.CharField()
    estados = forms.CharField(widget=forms.Select(choices=ESTADOS))

    Cventa.widget.attrs['class']= 'form-control'
    Cproductos.widget.attrs['class']= 'form-control'
    Descripcion.widget.attrs['class']= 'form-control'
    Cantidad.widget.attrs['class']= 'form-control'
    Categoria.widget.attrs['class']= 'form-control'

class FormProducto(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

class FormBoleta(forms.ModelForm):
    class Meta:
        model= Boleta
        fields ='__all__'

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


    