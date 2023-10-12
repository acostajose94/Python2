import pandas as pd

def procesar_datos_telefonos(archivo_entrada, archivo_salida, nombre_columna, columnas):
    # Leer el archivo Excel
    df = pd.read_excel(archivo_entrada)

    # Crea un nuevo DataFrame para almacenar los resultados
    nuevo_df = pd.DataFrame(columns=['EMPLID', nombre_columna])

    # Itera sobre cada fila del DataFrame original
    for index, row in df.iterrows():
        emplid = row['EMPLID']
        for columna in columnas:
            telefono = row[columna]
            if pd.notnull(telefono):
                nuevo_df = nuevo_df.append({'EMPLID': emplid, nombre_columna: telefono}, ignore_index=True)

    # Elimina las filas duplicadas
    nuevo_df = nuevo_df.drop_duplicates()

    # Muestra los primeros 12 resultados
    print(nuevo_df.head(12))

    # Guarda el nuevo DataFrame en un nuevo archivo Excel
    nuevo_df.to_excel(archivo_salida, index=False)
    
columnas_telefonos = ['TELEFONO3', 'TELEFONO4']
procesar_datos_telefonos('SELEC VIGENTE  _06.06.23.xlsx', 'resultado_panda.xlsx', 'TELEFONOS', columnas_telefonos)

# procesar_datos_telefonos(
#     'SELEC VIGENTE  _06.06.23.xlsx', 
#     'nuevo_nombre_del_archivo.xlsx', 
#     'CORREOS',
#     'EMAIL2',
#     'EMAIL3',
#     'EMAIL4'
#     )
