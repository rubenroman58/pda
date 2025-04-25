from django.shortcuts import render
from django.http import HttpResponse

def incrementar_visitas(request):
    # Verificamos si la sesión tiene la clave 'visitas'
    if 'visitas' in request.session:
        # Si la tiene, incrementamos el contador
        request.session['visitas'] += 1
    else:
        # Si no la tiene, inicializamos el contador de visitas
        request.session['visitas'] = 1

    # Devolvemos una respuesta mostrando el número de visitas
    return HttpResponse(f'Número de visitas: {request.session["visitas"]}')

def reiniciar_sesion(request):
    # Limpiar la sesión completamente
    request.session.flush()

    # Confirmamos que la sesión fue reiniciada
    return HttpResponse('La sesión ha sido reiniciada')
