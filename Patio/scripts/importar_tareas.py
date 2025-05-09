from pda.models import TipoTarea

# Lista de artículos con id, cod_tarea y nombre
articulos = [
    (101, 'FD', 'FUNDAS PUNTALES'),
    (102, 'CL', 'CLASIFICACION'),
    (103, 'RP', 'REPARACION'),
    (104, 'TR', 'TORITO'),
    (105, 'CM', 'CAMIONES'),
    (106, 'PG', 'PATIO GENERAL'),
    (107, 'PD', 'PEDIDOS'),
    (108, 'CP', 'COMPL PAQUETE'),
    (109, 'PINT', 'PINTURA'),
    (110, 'MM', 'MONTAR MURO')
]

# Insertar todos los artículos en la base de datos
for id_tarea, cod_tarea, nombre in articulos:
    TipoTarea.objects.create(id=id_tarea, cod_tarea=cod_tarea, nombre=nombre)
