from django.contrib import admin
from tiendaApp.models import Venta
from tiendaApp.models import Boleta
from tiendaApp.models import Usuario
from tiendaApp.models import Student

# Register your models here.
class VentaAdmin(admin.ModelAdmin):
    list_display=['id', 'Cventa', 'Cproductos', 'Descripcion', 'Cantidad', 'Categoria','PrecioT']

class BoletaAdmin(admin.ModelAdmin):
    list_display=['id','Nboleta','Rutl','DiLocal','fecha','telefono','NomLocal']

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['id','nombre','apellido','cargo','email','fono','direccion']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'score']

admin.site.register(Student, StudentAdmin)
admin.site.register(Venta,VentaAdmin)
admin.site.register(Boleta,BoletaAdmin)
admin.site.register(Usuario,UsuarioAdmin)