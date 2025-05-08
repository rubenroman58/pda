from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Patio,Paquete,AlbaranDevolucion,LineaArticulo,Articulo,TipoTarea,Trabajador
admin.site.register(Patio)
admin.site.register(Paquete)
admin.site.register(AlbaranDevolucion)
admin.site.register(LineaArticulo)
admin.site.register(Articulo)
admin.site.register(TipoTarea)

# Define la clase Resource para el modelo Trabajador
class TrabajadorResource(resources.ModelResource):
    class Meta:
        model = Trabajador

# Configura la administración de Trabajador con la opción de importación/exportación
@admin.register(Trabajador)
class TrabajadorAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TrabajadorResource  # Asocia el Resource con el modelo


