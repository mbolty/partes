from django.contrib import admin
from .models import Cliente, Tecnico, Producto, ParteTrabajo, DetalleParte
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Producto)
admin.site.register(ParteTrabajo)
admin.site.register(DetalleParte)
