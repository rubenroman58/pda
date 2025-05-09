import os
import sys
import django
import csv

# Paso 1: Añadir la carpeta base del proyecto al sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # scripts/
BASE_DIR = os.path.dirname(BASE_DIR)  # sube a la raíz del proyecto (donde está manage.py)
sys.path.append(BASE_DIR)

# Paso 2: Configurar correctamente el nombre del módulo settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Patio.settings')

# Paso 3: Inicializar Django
django.setup()

# Paso 4: Importar modelo
from pda.models import Articulo

# Paso 5: Ruta del CSV
csv_path = os.path.join(BASE_DIR, 'scripts', 'articulos.csv')  # Asegúrate de que esté en scripts/

# Paso 6: Leer y crear objetos
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Saltar encabezado

    for row in reader:
        if len(row) >= 2:
            articulo_id = int(row[0])
            nombre = row[1].strip()
            Articulo.objects.create(id=articulo_id, nombre=nombre)

print("✔ Artículos importados correctamente.")
