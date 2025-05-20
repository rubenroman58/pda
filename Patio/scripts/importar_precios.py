# ejemplo_importador.py
import pandas as pd
from django.db import transaction
from pda.models import Articulo, Costes

# Cargar el archivo Excel (usa la hoja que corresponda si hay varias)
df = pd.read_excel('STOCK MATERIAL 26-04-25 GLOBAL.xlsx', header=3, engine='openpyxl')  # Header en la fila 4 (índice 3)

# Recorremos cada fila a partir de ahí
with transaction.atomic():
    for _, row in df.iterrows():
        nombre_articulo = str(row['Nombre']).strip()
        precio = row['Coste Ud.']  # De la región que quieras (ej: Andalucía)

        if pd.isna(nombre_articulo) or pd.isna(precio):
            continue  # Saltar si faltan datos

        articulo_obj, _ = Articulo.objects.get_or_create(nombre=nombre_articulo)
        Costes.objects.create(articulo=articulo_obj, precio=precio)
