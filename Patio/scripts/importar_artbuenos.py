from pda.models import Articulo, Cataluña  

datos = [
    ("Tablero Tricapa VERSATEC 197x50cm ; Azul (1ª)", 55131, 10.91),
    ("Puntal INDE-K 3m ; Ø48/40 e2/2.5mm", 67911, 2.09),
    ("Puntal INDE-K 4m ; Ø48/40 e2/2.5mm", 37571, 2.52),
    ("Panel TEIDE 300x100cm", 1117, 70.48),
    ("Sopanda Extrema  VERSATEC ; L=4,00m ; 7A ; Blanco", 6660, 13.99),
    ("Sopanda Intermedia VERSATEC ; L=4,00m ; 7A ; Blanco", 8251, 11.03),
    ("Mordaza TEIDE", 13623, 5.38),
    ("Puntal INDE-K 5m ; Ø60/52 e2/2.5mm", 15268, 5.64),
    ("Apeo UNO97 ; L=197 cm ; Naranja", 20365, 1.72),
    ("Panel TEIDE 4C Ligero 300x60cm", 1022, 54.08),
    ("Arriostrador UNO97 ; L=4,00 m ; Naranja", 4733, 12.65),
    ("Tuerca Placa Articulada TEIDE Ø15mm", 16690, 2.50),
    ("Panel TEIDE 300x240cm", 267, 169.61),
    ("Contenedor INDE-K 130x76x82 cm", 1049, 23.22),
    ("Puntal INDE-K 6m ; Ø60/52 e2/2.5mm", 2920, 10.33),
    ("Tablero Tricapa VERSATEC 80x50cm ; Azul (1ª)", 20, 6.00),
    ("Panel TEIDE 300x120cm", 185, 79.48),
    ("Panel TEIDE 4C Ligero 300x80cm", 339, 70.93),
    ("Panel TEIDE 300x60cm", 228, 59.60),
    ("Panel Esquina TEIDE 300x38x30cm", 174, 100.90),
    ("Articulo Nuevo", 58, 0.00),
    ("Panel TEIDE 300x80cm", 163, 65.80),
    ("Sopanda QBETA2a ; L=4,00m ; Zincado Inde-K", 153, 52.21),
    ("Panel TEIDE 300x50cm", 1413, 11.48),
    ("Sopanda Extrema VERSATEC ; L=2,00 m ; Blanco", 235, 44.25),
    ("Chapa Pilar Serie Medium 3000x500mm", 527, 22.11),
    ("Consola TEIDE CT60", 1946, 6.30),
    ("Barandilla INDE-K ; L=250 cm ; Clase A", 1865, 8.69),
    ("Sopanda Intermedia VERSATEC ; L=2,00 m ; Blanco", 399, 12.18),
    ("Puntal Aluminio UL ; 6,0 - 4,5 m", 1122, 12.25),
    ("Sopanda Extrema VERSATEC ; L=3,00 m ; Blanco", 396, 15.71),
    ("Tabica VERSATEC 30cm ; L=2,00m", 2776, 4.60),
    ("Anclaje U TEIDE Ø15mm", 1353, 9.17),
    ("Triángulo Cimbra INDE-K ; 136x100 cm", 189, 46.29),
    ("Sopanda Intermedia VERSATEC ; L=3,00 m ; Blanco", 240, 38.73),
    ("Tablero Tricapa VERSATEC 98x50cm ; Azul (1ª)", 578, 8.50),
    ("Panel TEIDE 300x30cm", 127, 52.02),
    ("Gancho Elevación TEIDE ; CMU=1500 kg", 111, 64.06),
    ("Barandilla INDE-K ; L=300 cm ; Clase A", 28, 446.06),
    ("Panel TEIDE 300x40cm", 1383, 8.17),
    ("Panel Esquina TEIDE 100x38x30cm", 203, 40.54),
    ("Torre de Hormigonado 3+1 m", 1, 5.12),
    ("Arriostrador UNO97 ; L=2,00 m ; Naranja", 765, 3.81),
    ("Panel TEIDE 100x100cm", 126, 8.00),
    ("Cubeta VERSATEC 80x74x25cm", 411, 18.79),
    ("Puntal INDE-K 1,50m ; Ø48/40  2/2mm", 1486, 2.85),
    ("Tablero Tricapa VERSATEC 98x50cm ; Amarillo (1ª)", 36, 206.09),
    ("Panel TEIDE 4C Ligero 100x60cm", 873, 8.32),
    ("Puntal INDE-K 1m ; Ø48/40 e1.6/1.6mm", 271, 14.05),
    ("Escuadra TEIDE ; Módulo 1", 400, 12.00),
]

for nombre, unid, precio in datos:
    try:
        articulo = Articulo.objects.filter(nombre=nombre).first()
        Cataluña.objects.create(
            articulo=articulo,
            tot_unid=unid,
            p_alq_medio=precio
        )
    except Articulo.DoesNotExist:
        print(f"Articulo no encontrado: {nombre}")
