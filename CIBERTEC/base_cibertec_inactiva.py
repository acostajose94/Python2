import pandas as pd
import datetime
import os
import winreg
import shutil
from funciones_base import *

archivo1='Base Asignacion Inactiva II Mayo.xlsx'
archivo2='Base Asignacion Inactiva III Mayo.xlsx'
archivo3='Base Asignacion Inactiva IV Mayo.xlsx'
archivo4='Base Asignacion Diplomado, wetalk Mayo.xlsx'
archivo5='Base Asignacion Inactiva Formacion continua Mayo.xlsx'
#---------------------------

arch1=tabla_base(archivo1)
arch2=tabla_base(archivo2)
arch3=tabla_base(archivo3)
arch4=tabla_base(archivo4)
arch5=tabla_base(archivo5)


tabla_final = pd.concat([arch1,arch2,arch3,arch4,arch5])

# Obtener la fecha actual en formato dd_mm
fecha_actual = datetime.datetime.now().strftime('%d_%m')
ruta_carpeta = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Escritorio',  fecha_actual+'b cibert Inactiva')
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)

ruta_archivo = os.path.join(ruta_carpeta, fecha_actual+' Base Inactiva.xlsx')

tabla_final.to_excel(ruta_archivo, index=False)

shutil.move(archivo1,ruta_carpeta)
shutil.move(archivo2,ruta_carpeta)
shutil.move(archivo3,ruta_carpeta)
shutil.move(archivo4,ruta_carpeta)
shutil.move(archivo5,ruta_carpeta)