"""
URL configuration for Patio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import  admin
from django.urls import path
from pda.views import iniciar_tarea,eliminar_tarea,eliminar_alabarn,informacionIndek,detalles_albaran,lista_albaranes_completa,estadisticas_trabajador,detalles_tarea,lista_tareas_completa,lista_trabajadores,estadisticas,agregar_lineas,crear_paquete,home,salir,finalizar_tarea,seleccionar_albaran

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iniciar-tarea/', iniciar_tarea, name='iniciar_tarea'),
    path('crear-paquete/<int:tarea_id>/', crear_paquete, name='crear_paquete'),
    path('',home,name='home'),
    path('paginaInicial/',home),
    path('cerrar_programa/',salir),
    path('iniciar_tarea/',iniciar_tarea),
    path('finalizar-tarea/<int:tarea_id>/', finalizar_tarea, name='finalizar_tarea'),
    path('seleccionar_albaran/', seleccionar_albaran, name='seleccionar_albaran'),
    path('agregar_lineas/<int:albaran_id>/', agregar_lineas, name='agregar_lineas'),
    path('estadisticas/',estadisticas),
    path('estadisticasTrabajadores/',lista_trabajadores),
    path('lista_tareas/',lista_tareas_completa,name='listaTareas'),
    path('tarea/<int:tarea_id>/',detalles_tarea, name='detalle_tarea'),
    path('estadisticas_trabajador/<int:trabajador_id>/',estadisticas_trabajador,name='estadisticas_trabajador'),
    path('lista_albaranes/',lista_albaranes_completa, name='listaAlbaranes'),
    path('detalle_albaran/<int:albaran_id>/',detalles_albaran, name='detalle_albaran'),
    path('informacionIndek/',informacionIndek, name='informacionIndek'),
    path('eliminar_albaran/<int:albaran_id>/',eliminar_alabarn,name='eliminarAlbaran'),
    path('eliminar_tarea/<int:tarea_id>/',eliminar_tarea,name='eliminarTarea')    
]

