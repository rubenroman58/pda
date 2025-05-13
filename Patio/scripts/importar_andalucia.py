import pandas as pd
import os
import django

from pda.models import Andalucia,Articulo


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Patio.settings")
django.setup()

df = pd.read_excel('STOCK MATERIAL 26-04-25 GLOBAL.xlsx',header=2,usecols=[1, 4, 5])

# Renombramos las columnas para trabajar con nombres claros
df.columns=['nombre_articulo','tot_unid','p_alq_medio']

#Limpieza de datos
df['tot_unid'] = df['tot_unid'].astype(str).str.replace('.', '').str.replace(',', '').astype(int)
df['p_alq_medio'] = df['p_alq_medio'].astype(str).str.replace(',', '.').astype(float)

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
    