from nueva_variable_p import *
from nueva_funcion_p  import *
from formato_columnas import *
import os
import datetime
import shutil
import pandas as pd


acti='Activa_Junio'
# Procesar cada archivo de Excel
for archivo in archivos_excel2:
    resultado2 = procesar_archivo_excel(archivo)
    resultados2.append(resultado2)
# Combinar todos los DataFrames resultantes en uno solo
tabla_final2 = pd.concat(resultados2, ignore_index=True)
ruta_carpeta = verifica_carpeta(fecha_actual,acti)
print(ruta_carpeta)
print(fecha_actual)
print(acti)
ruta_archivo = os.path.join(ruta_carpeta, fecha_actual+' Pagos '+acti+'.xlsx')
tabla_final2.to_excel(ruta_archivo, index=False)
for archivo in archivos_excel2:
    shutil.move(archivo,ruta_carpeta)
formato_columnas(ruta_archivo)


inacti='inActiva_Junio'
# Procesar cada archivo de Excel
for archivo in archivos_excel:
    resultado = procesar_archivo_excel(archivo)
    resultados.append(resultado)
# Combinar todos los DataFrames resultantes en uno solo
tabla_final = pd.concat(resultados, ignore_index=True)
ruta_carpeta = verifica_carpeta(fecha_actual,inacti)
ruta_archivo = os.path.join(ruta_carpeta, fecha_actual+' Pagos '+inacti+'.xlsx')
tabla_final.to_excel(ruta_archivo, index=False)
for archivo in archivos_excel:
    shutil.move(archivo,ruta_carpeta)
formato_columnas(ruta_archivo)



# inacti='inActiva'
#  # Procesar cada archivo de Excel
# for archivo in archivos_excel:
#     resultado = procesar_archivo_excel(archivo)
#     nombre_archivo = os.path.basename(archivo)  # Obtener el nombre del archivo sin la ruta
#     ruta_carpeta = verifica_carpeta(fecha_actual, inacti)
#     ruta_archivo = os.path.join(ruta_carpeta, f'{nombre_archivo}_Resultado.xlsx')
    
#     # Guardar el resultado en un archivo separado
#     resultado.to_excel(ruta_archivo, index=False)
    
#     # Mover el archivo original a la carpeta de destino
#     shutil.move(archivo, ruta_carpeta)
    
#     # Aplicar el formato a las columnas en el archivo guardado
#     formato_columnas(ruta_archivo)