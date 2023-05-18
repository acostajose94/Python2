import pandas as pd
import datetime
import os
import winreg
import shutil
from funciones_base import *

archivo1='Asignacion Cartera Activa 2023-1 Mayo 17-31 Mayo.xlsx'

#---------------------------

arch1=tabla_base(archivo1)
tabla_final = pd.concat([arch1])

# Obtener la fecha actual en formato dd_mm
fecha_actual = datetime.datetime.now().strftime('%d_%m')
ruta_carpeta = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Escritorio',  fecha_actual+'b cibert Activa')
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)

ruta_archivo = os.path.join(ruta_carpeta, fecha_actual+' Base Activa.xlsx')

tabla_final.to_excel(ruta_archivo, index=False)

shutil.move(archivo1,ruta_carpeta)
