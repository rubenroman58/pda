from django.urls import path
from . import views

urlpatterns = [
    path('visitas/', views.incrementar_visitas),
    path('reiniciar/', views.reiniciar_sesion), 
]
