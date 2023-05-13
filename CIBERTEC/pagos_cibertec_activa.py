import pandas as pd
import datetime
import os
import winreg
import shutil
from completado_funcion import *

archivo1='Asignacion Cartera activa 2023-1 Mayo.xlsx'

#---------------------------
arch1=tabla(archivo1)

#tabla3=tabla('Base Asignacion Formacion continua Externa 2022  Enero.xlsx')

tabla_final = pd.concat([arch1])

# Obtener la fecha actual en formato dd_mm
fecha_actual = datetime.datetime.now().strftime('%d_%m')
# Crear la ruta de la carpeta en el escritorio con la fecha actual
# ruta_carpeta = os.path.join(os.path.expanduser('~'), 'Desktop',  fecha_actual+'p cibert')
# Este define la ruta si tienes onedrive, el anterior es si no lo tiene
ruta_carpeta = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Escritorio',  fecha_actual+'p cibert Activa')
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)

ruta_archivo = os.path.join(ruta_carpeta, fecha_actual+' Pagos Activa.xlsx')

tabla_final.to_excel(ruta_archivo, index=False)

shutil.move(archivo1,ruta_carpeta)
 