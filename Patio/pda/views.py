from django.shortcuts import render, redirect
from .models import Patio, Paquete,AlbaranDevolucion,LineaArticulo,TipoTarea,Trabajador,Articulo
from .forms import PatioForm, PaqueteForm,AlbaranForm,LineaArticulo,LineaArticuloForm
from datetime import datetime
from django.db.models import Sum  
from django.shortcuts import get_object_or_404


def iniciar_tarea(request):
    if request.method == 'POST':
        form = PatioForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.fecha = datetime.now().date()
            tarea.horaInicio = datetime.now().time().replace(microsecond=0)  
            tarea.save()  

        
            return redirect('crear_paquete', tarea_id=tarea.id)  
    else:
        form = PatioForm()

    trabajadores_dict = {trab.id: trab.nombre for trab in Trabajador.objects.all()}
    tipos_tarea_dict = {tipo.id: tipo.nombre for tipo in TipoTarea.objects.all()}

    return render(request, 'iniciar_tarea.html', {
        'form': form,
        'trabajadores': trabajadores_dict,
        'tipos_tarea': tipos_tarea_dict,
    })



def crear_paquete(request, tarea_id):
    tarea = get_object_or_404(Patio, id=tarea_id)

    if request.method == 'POST':
        form = PaqueteForm(request.POST)
        if form.is_valid():
            ahora = datetime.now().time().replace(microsecond=0)
            
            # Si es el primer paquete, usamos la hora de inicio de la tarea
            if not Paquete.objects.filter(tarea=tarea).exists():
                hora_inicio_paquete = tarea.horaInicio  # Para el primer paquete, la hora es la de la tarea
                hora_fin_paquete = ahora  # Hora de fin del primer paquete, la hora actual
            else:
                # Para los paquetes siguientes, la hora de inicio es la hora de fin del último paquete
                ultimo_paquete = Paquete.objects.filter(tarea=tarea).order_by('-id').first()
                hora_inicio_paquete = ultimo_paquete.horaFin  # La hora de inicio será la hora de fin del último paquete
                hora_fin_paquete = ahora  # La hora de fin será la hora actual

            # Crea el paquete sin guardarlo todavía
            paquete = form.save(commit=False)
            paquete.tarea = tarea
            paquete.horaInicio = hora_inicio_paquete  # Asignamos la hora de inicio al paquete
            paquete.horaFin = hora_fin_paquete  # Asignamos la hora de fin al paquete

            # Guardamos el paquete
            paquete.save()
            print(f"Nuevo paquete creado: horaInicio = {paquete.horaInicio}, horaFin = {paquete.horaFin}")

            # Si ya existía un paquete, actualizamos la hora de fin del paquete anterior
            if Paquete.objects.filter(tarea=tarea).count() > 1:
                ultimo_paquete = Paquete.objects.filter(tarea=tarea).order_by('-id').first()
                ultimo_paquete.horaFin = hora_fin_paquete  # El último paquete termina cuando empieza el nuevo
                ultimo_paquete.save()
                print(f"Hora fin del paquete anterior (ID {ultimo_paquete.id}) actualizada a {hora_fin_paquete}")

            # Actualizar la cantidad total
            total_cantidad = Paquete.objects.filter(tarea=tarea).aggregate(Sum('cantidad_paquete'))['cantidad_paquete__sum'] or 0
            tarea.cantidad = total_cantidad
            tarea.save()

            # Redirige a la misma página de crear paquete o a donde desees
            return redirect('crear_paquete', tarea_id=tarea.id)

        else:
            # Si el formulario no es válido, asegúrate de devolver una respuesta
            # En este caso, simplemente renderizamos el formulario con los errores
            articulos_dict = {art.id: art.nombre for art in Articulo.objects.all()}
            return render(request, 'crear_paquete.html', {
                'form': form,
                'tarea': tarea,
                'articulos': articulos_dict,
            })
    else:
        form = PaqueteForm()
        articulos_dict = {art.id: art.nombre for art in Articulo.objects.all()}
        return render(request, 'crear_paquete.html', {
            'form': form,
            'tarea': tarea,
            'articulos': articulos_dict,
        })


def finalizar_tarea(request, tarea_id):
    tarea = get_object_or_404(Patio, id=tarea_id)
    tarea.horaFin = datetime.now().time().replace(microsecond=0)  
    tarea.save()
    return redirect('iniciar_tarea') 


def seleccionar_albaran(request):
    if request.method == 'POST':
        form = AlbaranForm(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['numero']
            albaran, creado = AlbaranDevolucion.objects.get_or_create(numero=numero)
          
            return redirect('agregar_lineas', albaran_id=albaran.id)
        else:
            print("Este formulario ya ha sido creado:", form.errors)
    else:
        form = AlbaranForm()
    return render(request, 'seleccionar_albaran.html', {'form': form})


def home (request): 
    return render(request,'index.html')

def agregar_lineas(request,albaran_id):
    albaran = AlbaranDevolucion.objects.get(id=albaran_id)
    if request.method=='POST':
        form=LineaArticuloForm(request.POST)
        if form.is_valid():
         cantidad_buena= form.cleaned_data['cantidad_buena']
         cantidad_mala= form.cleaned_data['cantidad_mala']
         chatarra= form.cleaned_data['chatarra']
         idArticulo= form.cleaned_data['idArticulo']

         LineaArticulo.objects.create(
             albaran=albaran,
             idArticulo=idArticulo,
             cantidad_buena=cantidad_buena,
             chatarra=chatarra,
             cantidad_mala=cantidad_mala
         )
         return redirect('agregar_lineas', albaran_id=albaran.id)
    else:
        form = LineaArticuloForm()

    return render(request, 'agregar_lineas.html', {'form': form, 'albaran': albaran})
def salir(request):
    return render(request,'cerrar_programa.html')

def estadisticas(request):
    return render(request,'estadisticas.html')