import os
import sys
import django
import pandas as pd

# Paso 1: Añadir la carpeta base del proyecto al sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # scripts/
BASE_DIR = os.path.dirname(BASE_DIR)  # sube a la raíz del proyecto (donde está manage.py)
sys.path.append(BASE_DIR)

# Paso 2: Configurar correctamente el nombre del módulo settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Patio.settings')

# Paso 3: Inicializar Django
django.setup()

# Paso 4: Importar los modelos necesarios
from pda.models import Andalucia, Articulo

# Paso 5: Leer el archivo de Excel
ruta_excel = os.path.join(BASE_DIR, 'scripts', 'datos.xlsx')  # Asumiendo que el archivo está en scripts/
df = pd.read_excel(ruta_excel, header=2, usecols=[1, 4, 5])

# Paso 6: Renombrar las columnas para facilitar el trabajo
df.columns = ['nombre_articulo', 'tot_unid', 'p_alq_medio']

# Paso 7: Limpiar los datos
df['tot_unid'] = df['tot_unid'].astype(str).str.replace('.', '').str.replace(',', '').astype(int)
df['p_alq_medio'] = df['p_alq_medio'].astype(str).str.replace(',', '.').astype(float)

# Paso 8: Crear objetos en la base de datos
for index, row in df.iterrows():
    try:
        articulo, created = Articulo.objects.get_or_create(nombre=row['nombre_articulo'])
        Andalucia.objects.create(
            articulo=articulo,
            tot_unid=row['tot_unid'],
            p_alq_medio=row['p_alq_medio']
        )
    except Exception as e:
        print(f"Error en la fila {index}: {e}")

print("✔ Datos de Andalucia importados correctamente.")
