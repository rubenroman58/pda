from pda.models import Articulo, Levante

# Datos para Levante
datos_levante = [
    ("Tablero Tricapa VERSATEC 197x50cm ; Azul (1ª)", 51234, 11.25),
    ("Puntal INDE-K 3m ; Ø48/40 e2/2.5mm", 69301, 2.18),
    ("Puntal INDE-K 4m ; Ø48/40 e2/2.5mm", 38790, 2.65),
    ("Panel TEIDE 300x100cm", 950, 73.12),
    ("Sopanda Extrema  VERSATEC ; L=4,00m ; 7A ; Blanco", 6400, 14.50),
    ("Sopanda Intermedia VERSATEC ; L=4,00m ; 7A ; Blanco", 8195, 11.80),
    ("Mordaza TEIDE", 13850, 5.70),
    ("Puntal INDE-K 5m ; Ø60/52 e2/2.5mm", 15320, 5.90),
    ("Apeo UNO97 ; L=197 cm ; Naranja", 20875, 1.80),
    ("Panel TEIDE 4C Ligero 300x60cm", 980, 55.00),
    ("Arriostrador UNO97 ; L=4,00 m ; Naranja", 4750, 12.80),
    ("Tuerca Placa Articulada TEIDE Ø15mm", 16380, 2.60),
    ("Panel TEIDE 300x240cm", 280, 168.50),
    ("Contenedor INDE-K 130x76x82 cm", 1032, 23.60),
    ("Puntal INDE-K 6m ; Ø60/52 e2/2.5mm", 2940, 10.20),
    ("Tablero Tricapa VERSATEC 80x50cm ; Azul (1ª)", 30, 6.20),
    ("Panel TEIDE 300x120cm", 175, 80.90),
    ("Panel TEIDE 4C Ligero 300x80cm", 330, 71.80),
    ("Panel TEIDE 300x60cm", 220, 60.10),
    ("Panel Esquina TEIDE 300x38x30cm", 160, 98.70),
    ("Articulo Nuevo", 65, 0.00),
    ("Panel TEIDE 300x80cm", 145, 68.20),
    ("Sopanda QBETA2a ; L=4,00m ; Zincado Inde-K", 140, 54.50),
    ("Panel TEIDE 300x50cm", 1350, 11.40),
    ("Sopanda Extrema VERSATEC ; L=2,00 m ; Blanco", 220, 45.00),
    ("Chapa Pilar Serie Medium 3000x500mm", 500, 22.50),
    ("Consola TEIDE CT60", 1900, 6.50),
    ("Barandilla INDE-K ; L=250 cm ; Clase A", 1850, 8.90),
    ("Sopanda Intermedia VERSATEC ; L=2,00 m ; Blanco", 420, 12.50),
    ("Puntal Aluminio UL ; 6,0 - 4,5 m", 1130, 12.60),
    ("Sopanda Extrema VERSATEC ; L=3,00 m ; Blanco", 400, 15.90),
    ("Tabica VERSATEC 30cm ; L=2,00m", 2780, 4.75),
    ("Anclaje U TEIDE Ø15mm", 1365, 9.30),
    ("Triángulo Cimbra INDE-K ; 136x100 cm", 185, 45.10),
    ("Sopanda Intermedia VERSATEC ; L=3,00 m ; Blanco", 250, 37.50),
    ("Tablero Tricapa VERSATEC 98x50cm ; Azul (1ª)", 580, 8.75),
    ("Panel TEIDE 300x30cm", 130, 51.60),
    ("Gancho Elevación TEIDE ; CMU=1500 kg", 105, 63.80),
    ("Barandilla INDE-K ; L=300 cm ; Clase A", 35, 450.10),
    ("Panel TEIDE 300x40cm", 1400, 8.00),
    ("Panel Esquina TEIDE 100x38x30cm", 210, 39.60),
    ("Torre de Hormigonado 3+1 m", 2, 5.30),
    ("Arriostrador UNO97 ; L=2,00 m ; Naranja", 780, 3.90),
    ("Panel TEIDE 100x100cm", 120, 8.20),
    ("Cubeta VERSATEC 80x74x25cm", 420, 18.50),
    ("Puntal INDE-K 1,50m ; Ø48/40  2/2mm", 1500, 2.90),
    ("Tablero Tricapa VERSATEC 98x50cm ; Amarillo (1ª)", 40, 210.00),
    ("Panel TEIDE 4C Ligero 100x60cm", 850, 8.50),
    ("Puntal INDE-K 1m ; Ø48/40 e1.6/1.6mm", 275, 13.90),
    ("Escuadra TEIDE ; Módulo 1", 390, 12.20),
]

# Insertar datos para Levante
for nombre, unid, precio in datos_levante:
    articulo = Articulo.objects.filter(nombre=nombre).first()
    if articulo:
        Levante.objects.create(
            articulo=articulo,
            tot_unid=unid,
            p_alq_medio=precio
        )
    else:
        print(f"⚠️ Articulo no encontrado: {nombre}")
