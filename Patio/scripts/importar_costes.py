from pda.models import Articulo, Costes

datos = [
    ("Tablero Tricapa VERSATEC 197x50cm ; Azul (1ª)", 18.000),
    ("Puntal INDE-K 3m ; Ø48/40 e2/2.5mm", 19.100),
    ("Puntal INDE-K 4m ; Ø48/40 e2/2.5mm", 23.000),
    ("Panel TEIDE 300x100cm", 431.500),
    ("Sopanda Extrema  VERSATEC ; L=4,00m ; 7A ; Blanco", 54.100),
    ("Sopanda Intermedia VERSATEC ; L=4,00m ; 7A ; Blanco", 42.600),
    ("Mordaza TEIDE", 25.350),
    ("Puntal INDE-K 5m ; Ø60/52 e2/2.5mm", 38.500),
    ("Apeo UNO97 ; L=197 cm ; Naranja", 10.340),
    ("Panel TEIDE 4C Ligero 300x60cm", 279.530),
    ("Arriostrador UNO97 ; L=4,00 m ; Naranja", 38.700),
    ("Tuerca Placa Articulada TEIDE Ø15mm", 6.770),
    ("Panel TEIDE 300x240cm", 878.560),
    ("Contenedor INDE-K 130x76x82 cm", 118.600),
    ("Puntal INDE-K 6m ; Ø60/52 e2/2.5mm", 44.800),
    ("Tablero Tricapa VERSATEC 80x50cm ; Azul (1ª)", 9.400),
    ("Panel TEIDE 300x120cm", 496.870),
    ("Panel TEIDE 4C Ligero 300x80cm", 318.660),
    ("Panel TEIDE 300x60cm", 349.780),
    ("Panel Esquina TEIDE 300x38x30cm", 404.320),
    ("Articulo Nuevo", 438.310),
    ("Panel TEIDE 300x80cm", 49.900),
    ("Sopanda QBETA2a ; L=4,00m ; Zincado Inde-K", 356.910),
    ("Panel TEIDE 300x50cm", 27.970),
    ("Sopanda Extrema VERSATEC ; L=2,00 m ; Blanco", 203.000),
    ("Chapa Pilar Serie Medium 3000x500mm", 49.430),
    ("Consola TEIDE CT60", 8.140),
    ("Barandilla INDE-K ; L=250 cm ; Clase A", 21.520),
    ("Sopanda Intermedia VERSATEC ; L=2,00 m ; Blanco", 199.000),
    ("Puntal Aluminio UL ; 6,0 - 4,5 m", 41.240),
    ("Sopanda Extrema VERSATEC ; L=3,00 m ; Blanco", 42.000),
    ("Tabica VERSATEC 30cm ; L=2,00m", 7.400),
    ("Anclaje U TEIDE Ø15mm", 35.300),
    ("Triángulo Cimbra INDE-K ; 136x100 cm", 32.380),
    ("Sopanda Intermedia VERSATEC ; L=3,00 m ; Blanco", 9.000),
    ("Tablero Tricapa VERSATEC 98x50cm ; Azul (1ª)", 281.380),
    ("Panel TEIDE 300x30cm", 168.800),
    ("Gancho Elevación TEIDE ; CMU=1500 kg", 10.780),
    ("Barandilla INDE-K ; L=300 cm ; Clase A", 304.140),
    ("Panel TEIDE 300x40cm", 170.940),
    ("Panel Esquina TEIDE 100x38x30cm", 1.155),
    ("Torre de Hormigonado 3+1 m", 23.640),
    ("Arriostrador UNO97 ; L=2,00 m ; Naranja", 17.420),
    ("Panel TEIDE 100x100cm", 31.500),
    ("Cubeta VERSATEC 80x74x25cm", 12.900),
    ("Puntal INDE-K 1,50m ; Ø48/40 2/2mm", 12.300),
    ("Tablero Tricapa VERSATEC 98x50cm ; Amarillo (1ª)", 6.700),
    ("Panel TEIDE 4C Ligero 100x60cm", 14.800),
    ("Puntal INDE-K 1m ; Ø48/40 e1.6/1.6mm", 280.000),
    ("Escuadra TEIDE ; Módulo 1", 420.000),
]

# Recorremos los datos
for nombre, precio in datos:
    articulo = Articulo.objects.filter(nombre=nombre).first()
    
    if articulo:  # Si se encuentra el artículo
        try:
            Costes.objects.create(
                articulo=articulo,
                precio=precio
            )
            print(f"✔️ Coste creado para: {nombre}")
        except Exception as e:
            print(f"❌ Error al crear coste para {nombre}: {e}")
    else:
        print(f"⚠️ Articulo no encontrado: {nombre}")
