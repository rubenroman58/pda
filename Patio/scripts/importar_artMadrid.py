from pda.models import Articulo, Madrid

datos = [
    ("Tablero Tricapa VERSATEC 197x50cm ; Azul (1ª)", 51000, 10.65),
    ("Puntal INDE-K 3m ; Ø48/40 e2/2.5mm", 67000, 2.25),
    ("Puntal INDE-K 4m ; Ø48/40 e2/2.5mm", 35000, 2.40),
    ("Panel TEIDE 300x100cm", 1150, 68.50),
    ("Sopanda Extrema  VERSATEC ; L=4,00m ; 7A ; Blanco", 6200, 14.10),
    ("Sopanda Intermedia VERSATEC ; L=4,00m ; 7A ; Blanco", 7900, 10.85),
    ("Mordaza TEIDE", 13900, 5.45),
    ("Puntal INDE-K 5m ; Ø60/52 e2/2.5mm", 14800, 5.75),
    ("Apeo UNO97 ; L=197 cm ; Naranja", 20500, 1.70),
    ("Panel TEIDE 4C Ligero 300x60cm", 1080, 54.20),
    ("Arriostrador UNO97 ; L=4,00 m ; Naranja", 4600, 12.50),
    ("Tuerca Placa Articulada TEIDE Ø15mm", 16700, 2.55),
    ("Panel TEIDE 300x240cm", 280, 168.00),
    ("Contenedor INDE-K 130x76x82 cm", 1070, 23.00),
    ("Puntal INDE-K 6m ; Ø60/52 e2/2.5mm", 3100, 10.80),
    ("Tablero Tricapa VERSATEC 80x50cm ; Azul (1ª)", 22, 6.10),
    ("Panel TEIDE 300x120cm", 190, 77.20),
    ("Panel TEIDE 4C Ligero 300x80cm", 330, 71.00),
    ("Panel TEIDE 300x60cm", 220, 59.80),
    ("Panel Esquina TEIDE 300x38x30cm", 180, 99.50),
    ("Articulo Nuevo", 55, 1.10),
    ("Panel TEIDE 300x80cm", 155, 65.00),
    ("Sopanda QBETA2a ; L=4,00m ; Zincado Inde-K", 150, 53.50),
    ("Panel TEIDE 300x50cm", 1450, 11.00),
    ("Sopanda Extrema VERSATEC ; L=2,00 m ; Blanco", 245, 44.50),
    ("Chapa Pilar Serie Medium 3000x500mm", 510, 21.90),
    ("Consola TEIDE CT60", 1920, 6.50),
    ("Barandilla INDE-K ; L=250 cm ; Clase A", 1850, 8.80),
    ("Sopanda Intermedia VERSATEC ; L=2,00 m ; Blanco", 420, 11.70),
    ("Puntal Aluminio UL ; 6,0 - 4,5 m", 1180, 12.20),
    ("Sopanda Extrema VERSATEC ; L=3,00 m ; Blanco", 405, 15.30),
    ("Tabica VERSATEC 30cm ; L=2,00m", 2750, 4.50),
    ("Anclaje U TEIDE Ø15mm", 1320, 9.00),
    ("Triángulo Cimbra INDE-K ; 136x100 cm", 200, 47.00),
    ("Sopanda Intermedia VERSATEC ; L=3,00 m ; Blanco", 235, 37.80),
    ("Tablero Tricapa VERSATEC 98x50cm ; Azul (1ª)", 590, 8.30),
    ("Panel TEIDE 300x30cm", 135, 50.90),
    ("Gancho Elevación TEIDE ; CMU=1500 kg", 120, 62.00),
    ("Barandilla INDE-K ; L=300 cm ; Clase A", 33, 440.00),
    ("Panel TEIDE 300x40cm", 1450, 8.10),
    ("Panel Esquina TEIDE 100x38x30cm", 210, 39.50),
    ("Torre de Hormigonado 3+1 m", 3, 4.80),
    ("Arriostrador UNO97 ; L=2,00 m ; Naranja", 760, 3.70),
    ("Panel TEIDE 100x100cm", 118, 7.90),
    ("Cubeta VERSATEC 80x74x25cm", 405, 18.30),
    ("Puntal INDE-K 1,50m ; Ø48/40  2/2mm", 1520, 2.90),
    ("Tablero Tricapa VERSATEC 98x50cm ; Amarillo (1ª)", 38, 207.00),
    ("Panel TEIDE 4C Ligero 100x60cm", 860, 8.40),
    ("Puntal INDE-K 1m ; Ø48/40 e1.6/1.6mm", 275, 13.80),
    ("Escuadra TEIDE ; Módulo 1", 420, 11.90),
]

for nombre, unid, precio in datos:
    articulo = Articulo.objects.filter(nombre=nombre).first()
    if articulo:
        Madrid.objects.create(
            articulo=articulo,
            tot_unid=unid,
            p_alq_medio=precio
        )
    else:
        print(f"⚠️ Articulo no encontrado: {nombre}")
