from django.shortcuts import render, redirect
from datetime import datetime,timedelta,date
from django.db.models import Sum,Q
from django.shortcuts import get_object_or_404
from .models import Patio, Paquete,AlbaranDevolucion,LineaArticulo,TipoTarea,Trabajador,Articulo
from .forms import PatioForm,PaqueteForm,AlbaranForm,LineaArticulo,LineaArticuloForm,TrabajadorForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.forms import modelformset_factory

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
            return render(request,'agregar_lineas.html',{
                'form':form,
                'albaran':albaran,
                'articulos':{art.id: art.nombre for art in Articulo.objects.all()},
            })
    else:
        form = LineaArticuloForm()
        articulos_dict = {art.id: art.nombre for art in Articulo.objects.all()}
        return render(request, 'agregar_lineas.html', {
            'form': form, 
            'albaran': albaran,
            'articulos':articulos_dict
             })
    

def agregar_lineas2(request,albaran_id):
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
         return redirect('añadir_lineas', albaran_id=albaran.id)
        else:           
            return render(request,'añadir_linea.html',{
                'form':form,
                'albaran':albaran,
                'articulos':{art.id: art.nombre for art in Articulo.objects.all()},
            })
    else:
        form = LineaArticuloForm()
        articulos_dict = {art.id: art.nombre for art in Articulo.objects.all()}
        return render(request, 'añadir_linea.html', {
            'form': form, 
            'albaran': albaran,
            'articulos':articulos_dict
             })
    


def salir(request):
    return render(request,'cerrar_programa.html')

def estadisticas(request):

    return render(request,'estadisticas.html')

def lista_trabajadores(request):
    trabajadores=Trabajador.objects.all()

    trabajadores_lista=[]
    for tra in trabajadores:
        trabajador_lista={
           'id':tra.id,
           'nombre':tra.nombre
        }
        trabajadores_lista.append(trabajador_lista)

    return render(request,'lista_trabajadores.html',
                   {
                       'trabajadores_lista':trabajadores_lista
                   })

def lista_tareas_completa(request):
    tareas = Patio.objects.all().order_by('-fecha')
    
    tareas_info = []
    for tarea in tareas:
        tarea_info = {
            'id': tarea.id,
            'fecha': tarea.fecha,
            'horaInicio': tarea.horaInicio,
            'horaFin': tarea.horaFin,
            'tipo_tarea': TipoTarea.objects.filter(id=tarea.idTipTarea).first(),
            'operador1': Trabajador.objects.filter(id=tarea.idOper1).first(),
            'operador2': Trabajador.objects.filter(id=tarea.idOper2).first() if tarea.idOper2 else None,
            'cantidad': tarea.cantidad
        }
        tareas_info.append(tarea_info)

    return render(request, 'lista_tareas.html', {
        'tareas_info': tareas_info
    })
def detalles_tarea(request,tarea_id):
    tarea=get_object_or_404(Patio,id=tarea_id)
    paquetes=Paquete.objects.filter(tarea=tarea)
    volver_url = request.META.get('HTTP_REFERER', '/lista_tareas/')
    return render(request,'detalle_tarea.html',{
        'tarea':tarea,
        'paquetes':paquetes,
        'volver_url':volver_url
        })

def estadisticas_trabajador(request,trabajador_id):

    trabajador=get_object_or_404(Trabajador, id=trabajador_id)
    tareas=Patio.objects.filter(Q(idOper1=trabajador_id)| Q( idOper2=trabajador_id))
    periodo=request.GET.get('periodo')
    hoy=date.today()
    cantidadTotal=0
    tiempoTotalSegundos=0
    productividad=0
    numTareas=0
    tiempoPromedio=0
  
  
    
    for tarea in tareas:            
            if tarea.horaInicio and tarea.horaFin:
                fecha=tarea.fecha
                hora_inicio=datetime.combine(fecha,tarea.horaInicio)
                hora_fin=datetime.combine(fecha,tarea.horaFin)
                tiempoSegundos = (hora_fin - hora_inicio).total_seconds()
                tiempoTotalSegundos+= tiempoSegundos
    horas = int(tiempoTotalSegundos // 3600)
    minutos = int((tiempoTotalSegundos % 3600) // 60)
    segundos = int(tiempoTotalSegundos % 60)

    tiempoFinal = f"{horas:02d}:{minutos:02d}:{segundos:02d}"



    if periodo =='dia':

        tareas=tareas.filter(fecha=hoy)
        cantidadTotal=sum(tarea.cantidad or 0 for tarea in tareas)
        numTareas=tareas.count()

        
        if tiempoTotalSegundos >0:
            productividad=round(cantidadTotal/(tiempoTotalSegundos/3600),2)
        else:
            productividad=0

        if numTareas > 0:
            tiempoPromedioSegundos = tiempoTotalSegundos / numTareas
            horas = int(tiempoPromedioSegundos // 3600)
            minutos = int((tiempoPromedioSegundos % 3600) // 60)
            segundos = int(tiempoPromedioSegundos % 60)
            tiempoPromedio = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        else:
            tiempoPromedio = "00:00:00"
    
    elif periodo == 'semana':
      
      inicio_semana = hoy - timedelta(days=hoy.weekday())  # Primer día de la semana
      tareas = tareas.filter(fecha__gte=inicio_semana, fecha__lte=hoy)  # Filtrar tareas de la semana
      cantidadTotal=sum(tarea.cantidad or 0 for tarea in tareas)
      numTareas=tareas.count()
   
      if tiempoTotalSegundos >0:
            productividad=round(cantidadTotal/(tiempoTotalSegundos/3600),2)
      else:
            productividad=0

      if numTareas > 0:
            tiempoPromedioSegundos = tiempoTotalSegundos / numTareas
            horas = int(tiempoPromedioSegundos // 3600)
            minutos = int((tiempoPromedioSegundos % 3600) // 60)
            segundos = int(tiempoPromedioSegundos % 60)
            tiempoPromedio = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
      else:
            tiempoPromedioTarea = "00:00:00"
    
    elif periodo == 'mes':

        tareas = tareas.filter(fecha__month=hoy.month, fecha__year=hoy.year)
        cantidadTotal=sum(tarea.cantidad or 0 for tarea in tareas)
        numTareas=tareas.count()
        
        
        if tiempoTotalSegundos >0:
            productividad=round(cantidadTotal/(tiempoTotalSegundos/3600),2)
        else:
            productividad=0
        
        if numTareas > 0:
            tiempoPromedioSegundos = tiempoTotalSegundos / numTareas
            horas = int(tiempoPromedioSegundos // 3600)
            minutos = int((tiempoPromedioSegundos % 3600) // 60)
            segundos = int(tiempoPromedioSegundos % 60)
            tiempoPromedioTarea = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        else:
            tiempoPromedioTarea = "00:00:00"

    elif periodo =='todo':

        cantidadTotal=sum(tarea.cantidad or 0 for tarea in tareas)
        numTareas=tareas.count()
        
        
        if tiempoTotalSegundos >0:
            productividad=round(cantidadTotal/(tiempoTotalSegundos/3600),2)
        else:
            productividad=0
        
        if numTareas > 0:
            tiempoPromedioSegundos = tiempoTotalSegundos / numTareas
            horas = int(tiempoPromedioSegundos // 3600)
            minutos = int((tiempoPromedioSegundos % 3600) // 60)
            segundos = int(tiempoPromedioSegundos % 60)
            tiempoPromedio = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        else:
            tiempoPromedio = "00:00:00"

    
    return render(request,'estadisticas_trabajador.html',{
        'trabajador':trabajador,
        'tareas':tareas,
        'tiempo_total':tiempoFinal,
        'cantidad_total':cantidadTotal,
        'productividad':productividad,
        'numTareas':numTareas,
        'tiempoPromedio':tiempoPromedio
    })


def lista_albaranes_completa(request):

    listaAlbaranes=AlbaranDevolucion.objects.all().order_by('-fecha')
    albaranesinfo=[]
    for albaran in listaAlbaranes:
        albaraninfo={
        'id':albaran.id,
        'numero': albaran.numero,
        'fecha':albaran.fecha
        }
        albaranesinfo.append(albaraninfo)
    return render (request,'lista_albaranes.html',{
        'albaranesinfo':albaranesinfo
    }) 

def detalles_albaran(request,albaran_id):
    albaran=get_object_or_404(AlbaranDevolucion,id=albaran_id)
    articulos=LineaArticulo.objects.filter(albaran=albaran) #Obtenemos las lineas asociadas al albaran
    articulos_dict = {art.id: art.nombre for art in Articulo.objects.all()}
    for linea in articulos:
        linea.nombre_articulo=articulos_dict.get(linea.idArticulo)
    return render(request,'detalle_albaran.html',{
        'albaran':albaran,
        'articulos':articulos,
    })

def informacionIndek(request):

    return render(request,'informacionIndek.html')

def eliminar_alabarn(request, albaran_id):
    albaran = get_object_or_404(AlbaranDevolucion, id=albaran_id)
    albaran.delete()
    return redirect('listaAlbaranes')

def eliminar_tarea(request,tarea_id):
    tarea=get_object_or_404(Patio,id=tarea_id)
    tarea.delete()
    return redirect('listaTareas')

@csrf_exempt 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('Login correcto')
            return redirect('home')  # Esto depende de que la URL 'index' esté definida en tu URLconf
        else:
            print('Login fallido')
            messages.error(request, 'Usuario o contraseña incorrecta')

    return render(request, 'login.html')
    
def editar_linea_articulo(request, linea_id):
    linea = get_object_or_404(LineaArticulo, id=linea_id)
    albaran = linea.albaran

    if request.method == 'POST':
        form = LineaArticuloForm(request.POST, instance=linea)
        if form.is_valid():
            form.save()
            return redirect('detalle_albaran', albaran_id=albaran.id)
    else:
        form = LineaArticuloForm(instance=linea)

    return render(request, 'editar_linea.html', {
        'form': form,
        'albaran': albaran
    })


def eliminar_linea_articulo(request, linea_id):
    linea = get_object_or_404(LineaArticulo, id=linea_id)
    albaran_id = linea.albaran.id
    linea.delete()
    return redirect('detalle_albaran', albaran_id=albaran_id)
