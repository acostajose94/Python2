import pandas as pd
from nueva_funcion_b import *
from nueva_variables_b import *
import shutil
# Lista para almacenar los DataFrames modificados

# Aplicar la función a cada archivo de Excel
for archivo in archivos_excel:
    df_modificado = reordenar_columnas_y_guardar(archivo)
    dfs_modificados.append(df_modificado)

# Concatenar los DataFrames modificados en uno solo
df_concatenado = pd.concat(dfs_modificados)


carpeta=verifica_carpeta(fecha_actual,'INACTIVA')
# Guardar el DataFrame concatenado en un archivo Excel

ruta_archivo = os.path.join(carpeta, fecha_actual+' Base Inactiva.xlsx')
df_concatenado.to_excel('Base Inactiva3.xlsx', index=False)

# for a in archivos_excel:
#     shutil.move(a,ruta_archivo)


# Aplicar la función a cada archivo de Excel
for archivo2 in archivos_excel2:
    df_modificado2 = reordenar_columnas_y_guardar(archivo2)
    dfs_modificados2.append(df_modificado2)

# Concatenar los DataFrames modificados en uno solo
df_concatenado2 = pd.concat(dfs_modificados2)


carpeta2=verifica_carpeta(fecha_actual,'ACTIVA')
# Guardar el DataFrame concatenado en un archivo Excel

ruta_archivo2 = os.path.join(carpeta2, fecha_actual+' Base activa.xlsx')
df_concatenado2.to_excel('Base activa.xlsx', index=False)

for a in archivos_excel2:
    shutil.move(a,ruta_archivo2)
