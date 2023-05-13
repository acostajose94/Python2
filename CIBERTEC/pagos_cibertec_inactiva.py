import pandas as pd
import datetime
import os
import winreg
import shutil
from completado_funcion import *

archivo1='Base Asignacion Inactiva II Mayo.xlsx'
archivo2='Base Asignacion Inactiva III Mayo.xlsx'
archivo5='Base Asignacion Inactiva IV Mayo.xlsx'
archivo3='Base Asignacion Diplomado, wetalk Mayo.xlsx'
archivo4='Base Asignacion Inactiva Formacion continua Mayo.xlsx'
#---------------------------
arch5=tabla(archivo5)
arch1=tabla(archivo1)
arch2=tabla(archivo2)
arch3=tabla(archivo3)
arch4=tabla(archivo4)

#tabla3=tabla('Base Asignacion Formacion continua Externa 2022  Enero.xlsx')

tabla_final = pd.concat([arch1,arch2,arch3,arch4,arch5])

# Obtener la fecha actual en formato dd_mm
fecha_actual = datetime.datetime.now().strftime('%d_%m')
# Crear la ruta de la carpeta en el escritorio con la fecha actual
# ruta_carpeta = os.path.join(os.path.expanduser('~'), 'Desktop',  fecha_actual+'p cibert')
# Este define la ruta si tienes onedrive, el anterior es si no lo tiene
ruta_carpeta = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Escritorio',  fecha_actual+'p cibert Inactiva')
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)

ruta_archivo = os.path.join(ruta_carpeta, fecha_actual+' Pagos Inactiva.xlsx')

tabla_final.to_excel(ruta_archivo, index=False)

shutil.move(archivo1,ruta_carpeta)
shutil.move(archivo2,ruta_carpeta)
shutil.move(archivo3,ruta_carpeta)
shutil.move(archivo4,ruta_carpeta)
shutil.move(archivo5,ruta_carpeta)