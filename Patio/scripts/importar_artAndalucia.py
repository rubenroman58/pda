from pda.models import Articulo, Andalucia

datos = [
    ("Tablero Tricapa VERSATEC 197x50cm ; Azul (1ª)", 52700, 10.75),
    ("Puntal INDE-K 3m ; Ø48/40 e2/2.5mm", 69000, 2.15),
    ("Puntal INDE-K 4m ; Ø48/40 e2/2.5mm", 36000, 2.49),
    ("Panel TEIDE 300x100cm", 1200, 69.80),
    ("Sopanda Extrema  VERSATEC ; L=4,00m ; 7A ; Blanco", 6400, 14.30),
    ("Sopanda Intermedia VERSATEC ; L=4,00m ; 7A ; Blanco", 8000, 10.90),
    ("Mordaza TEIDE", 14000, 5.50),
    ("Puntal INDE-K 5m ; Ø60/52 e2/2.5mm", 14900, 5.80),
    ("Apeo UNO97 ; L=197 cm ; Naranja", 21000, 1.65),
    ("Panel TEIDE 4C Ligero 300x60cm", 1100, 53.50),
    ("Arriostrador UNO97 ; L=4,00 m ; Naranja", 4500, 12.80),
    ("Tuerca Placa Articulada TEIDE Ø15mm", 17000, 2.60),
    ("Panel TEIDE 300x240cm", 250, 170.00),
    ("Contenedor INDE-K 130x76x82 cm", 1050, 22.80),
    ("Puntal INDE-K 6m ; Ø60/52 e2/2.5mm", 3000, 10.70),
    ("Tablero Tricapa VERSATEC 80x50cm ; Azul (1ª)", 18, 6.20),
    ("Panel TEIDE 300x120cm", 200, 78.00),
    ("Panel TEIDE 4C Ligero 300x80cm", 320, 71.50),
    ("Panel TEIDE 300x60cm", 240, 60.00),
    ("Panel Esquina TEIDE 300x38x30cm", 160, 101.20),
    ("Articulo Nuevo", 60, 1.00),
    ("Panel TEIDE 300x80cm", 150, 64.90),
    ("Sopanda QBETA2a ; L=4,00m ; Zincado Inde-K", 145, 53.00),
    ("Panel TEIDE 300x50cm", 1400, 11.10),
    ("Sopanda Extrema VERSATEC ; L=2,00 m ; Blanco", 250, 43.70),
    ("Chapa Pilar Serie Medium 3000x500mm", 500, 22.00),
    ("Consola TEIDE CT60", 1900, 6.45),
    ("Barandilla INDE-K ; L=250 cm ; Clase A", 1800, 8.80),
    ("Sopanda Intermedia VERSATEC ; L=2,00 m ; Blanco", 410, 11.95),
    ("Puntal Aluminio UL ; 6,0 - 4,5 m", 1150, 12.10),
    ("Sopanda Extrema VERSATEC ; L=3,00 m ; Blanco", 400, 15.20),
    ("Tabica VERSATEC 30cm ; L=2,00m", 2800, 4.55),
    ("Anclaje U TEIDE Ø15mm", 1300, 9.30),
    ("Triángulo Cimbra INDE-K ; 136x100 cm", 195, 46.80),
    ("Sopanda Intermedia VERSATEC ; L=3,00 m ; Blanco", 230, 38.00),
    ("Tablero Tricapa VERSATEC 98x50cm ; Azul (1ª)", 600, 8.45),
    ("Panel TEIDE 300x30cm", 130, 51.50),
    ("Gancho Elevación TEIDE ; CMU=1500 kg", 115, 63.00),
    ("Barandilla INDE-K ; L=300 cm ; Clase A", 30, 445.00),
    ("Panel TEIDE 300x40cm", 1400, 8.30),
    ("Panel Esquina TEIDE 100x38x30cm", 200, 41.00),
    ("Torre de Hormigonado 3+1 m", 2, 5.00),
    ("Arriostrador UNO97 ; L=2,00 m ; Naranja", 750, 3.90),
    ("Panel TEIDE 100x100cm", 120, 8.10),
    ("Cubeta VERSATEC 80x74x25cm", 400, 18.50),
    ("Puntal INDE-K 1,50m ; Ø48/40  2/2mm", 1500, 2.95),
    ("Tablero Tricapa VERSATEC 98x50cm ; Amarillo (1ª)", 40, 205.00),
    ("Panel TEIDE 4C Ligero 100x60cm", 850, 8.50),
    ("Puntal INDE-K 1m ; Ø48/40 e1.6/1.6mm", 280, 13.95),
    ("Escuadra TEIDE ; Módulo 1", 420, 12.10),
]

for nombre, unid, precio in datos:
    articulo = Articulo.objects.filter(nombre=nombre).first()
    if articulo:
        Andalucia.objects.create(
            articulo=articulo,
            tot_unid=unid,
            p_alq_medio=precio
        )
    else:
        print(f"⚠️ Articulo no encontrado: {nombre}")
