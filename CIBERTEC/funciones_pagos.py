import pandas as pd
import re

# Completo
def convertir_a_float(df, columna):
    # convertir columna a tipo str
    df[columna] = df[columna].astype(str)
    # reemplazar coma por punto
    df[columna] = df[columna].str.replace(',', '.')
    # convertir a tipo float
    df[columna] = df[columna].astype(float)
    return df

def convertir_fecha(fecha):
    try:
        return fecha.strftime('%d/%m/%Y')
    except:
        return fecha
 
# PAgos
def tabla(archivo):
    # Leer el archivo de Excel
    df = pd.read_excel(archivo, sheet_name='Base de datos', header=1)
    # Reemplazar la palabra "Importe" por "IMPORTE" en las columnas
    df.columns = df.columns.str.replace('Importe', 'IMPORTE')
    nuevas_columnas = []
    for col in df.columns:
        if 'Importe' in col:
            nuevas_columnas.append(col.replace('Importe', 'IMPORTE'))
        elif 'Fecha' in col and col not in ['FECHADocumento', 'FECHAVencimiento']:
            if col.endswith('Fecha') or '.' in col:
                nuevas_columnas.append(col.replace('Fecha', 'FECHA'))
            else:
                nuevas_columnas.append(col)
        else:
            nuevas_columnas.append(col)

    # Asignar las nuevas columnas al DataFrame
    df.columns = nuevas_columnas
    print(df.columns)   
    if 'IMPORTE' not in df.columns:
        print('Nell')
        return None
    else:
        if 'N° Boleta ' not in df.columns:
            df = df.rename(columns={'N° Boleta': 'N° Boleta '})
            
        #Elimina columna 
        df = df.drop(columns=['COBRANZA'])
        df = df.rename(columns={'Gestor': 'GESTOR'})
        # Convertir la columna "GESTOR" a mayuscula
        df['GESTOR'] = df['GESTOR'].str.lower()

        # # Filtrar por los registros donde "GESTOR" es igual a "AVAL" en mayuscula
        # df = df[df['GESTOR'] == 'aval']
        # Filtrar por los registros que contienen la palabra "aval" en cualquier posición
        df = df[df['GESTOR'].str.contains('aval', case=False)]
        
        if 'Descripcion de Servicio' not in df.columns:
            df.insert(0, 'Descripcion de Servicio', '')
        if 'Correo 2' not in df.columns:
            df.insert(0, 'Correo 2', '')
        if 'FechaDocum' in df.columns and 'NumeroDocumentoIdentidad' in df.columns:
            df = df.rename(columns={
                'FechaDocum': 'FechaDocumento',
                'NumeroDocumentoIdentidad': 'NumeroDocumentoIdentidad1'
            })
        
        
        # Renombrar las columnas
        df = df.rename(columns={'IMPORTE': 'IMPORTE.0', 'FECHA': 'FECHA.0'})
        df_final = pd.DataFrame()
        
        
        # Obtener la última columna del dataframe
        ultima_columna = df.columns[-1]
        #Agarra todos los valores desde => . hacia la derecha
        ultimo_numero = ultima_columna.split(".")[-1]
        # print(df_final)
        # Sumar un número más a cada uno de los valores
        resultado = int(ultimo_numero) + 1


        for i in range(0, resultado):
            df_temp = df[['TipoDocumento', 'NumeroDocumento', 'N° Boleta ','GESTOR', 'GESTOR', 'Sede', 'FechaDocumento', 'FechaVencimiento', 'Año deuda',
                    'ClienteNombre', 'ClienteRUC', 'TipoVenta', 'Documento', 'FormadePago', 'MonedaDocumento', 'MontoTotal',
                    'MontoPagado', 'MontoPendiente', 'NombreCompleto', 'Criteria', 'UNIDAD', 'Teléfono 1', 'Teléfono 2',
                    'Correo 1 ', 'Correo 2', 'Tipo Documento Identidad', 'NumeroDocumentoIdentidad1', 'Descripcion de Servicio','GESTOR','GESTOR','GESTOR','GESTOR',
                    f'IMPORTE.{i}', f'FECHA.{i}']]
            df_temp.columns = ['TIPO', 'NUMERO_DOCUMENTO', 'BOLETA', 'GESTOR', 'BUCKET', 'SEDE', 'FECHA_DOC', 'FECHA_VEN', 'ANIO_DEUDA', 
                    'CLIENTE_NOM', 'CLIENTE_RUC', 'TIPO_VENTA', 'CODIGO_ALUMNO__RUC', 'FORMA_PAGO', 'MONEDA_DOC', 'MONTO_TOTAL', 
                    'MONTO_PAGADO', 'SALDO', 'NOMBRE_COMPLETO', 'CRITERIA', 'UNIDAD', 'TELEFONO_CASA2', 'CELULAR2',
                    'CORREO', 'CORREO2', 'TIPO_DOCUMENTO_IDENTIDAD', 'NUMERODOCUMENTOIDENTIDAD', 'DESCRIPCION_DE_SERVICIO', 'PERIODO', 'CICLO', 'PROMEDIO', 'PORCENT_CONDONACION', 'IMPORTE_PAGO', 'FECHA_PAGO']
            df_final = pd.concat([df_final, df_temp], axis=0, ignore_index=True)

        df_final = df_final.dropna(subset=['IMPORTE_PAGO'])

        #Poner en blanco
        df_final['BUCKET'] = pd.np.nan
        df_final['PORCENT_CONDONACION'] = pd.np.nan
        df_final['PROMEDIO'] = pd.np.nan
        df_final['CICLO'] = pd.np.nan
        df_final['PERIODO'] = pd.np.nan
        
        # #Modifica fecha, para completar
        # def convertir_fecha(fecha):
        #     try:
        #         return fecha.strftime('%d/%m/%Y')
        #     except:
        #         return fecha
        # df_final['FECHA_DOC'] = df_final['FECHA_DOC'].apply(convertir_fecha)
        # Convert the 'FECHA_DOC' column to a string data type
        df_final['FECHA_DOC'] = df_final['FECHA_DOC'].astype(str)
        mask = df_final['FECHA_DOC'].str.endswith('/202')
        filas = df_final[mask].index
        df_final.loc[filas, 'FECHA_DOC'] = df_final.loc[filas, 'FECHA_DOC'].apply(lambda x: x + '2') 
        
        def convertir_formato_fecha(fecha):
            patrones = [
                r'\d{2}/\d{2}/\d{4}',  # formato 'dd/mm/yyyy'
                r'\d{4}-\d{2}-\d{2}',  # formato 'yyyy-mm-dd'
            ]

            for patron in patrones:
                coincidencia = re.match(patron, fecha)
                if coincidencia:
                    fecha_match = coincidencia.group()
                    if '/' in fecha_match:
                        nueva_fecha = pd.to_datetime(fecha_match, format='%d/%m/%Y')
                    else:
                        nueva_fecha = pd.to_datetime(fecha_match, format='%Y-%m-%d')
                    return nueva_fecha.strftime('%d/%m/%Y')

            return fecha
            
        df_final['FECHA_DOC'] = df_final['FECHA_DOC'].apply(convertir_formato_fecha)
        df_final['FECHA_DOC'] = pd.to_datetime(df_final['FECHA_DOC'], format='%d/%m/%Y')

        #Regresa gestor a capitalize
        df_final['GESTOR'] = df_final['GESTOR'].str.title()
        
        df_final = convertir_a_float(df_final, 'MONTO_TOTAL')
        df_final = convertir_a_float(df_final, 'MONTO_PAGADO')
        df_final = convertir_a_float(df_final, 'SALDO')

        return df_final

# def tabla2(archivo):
#     # Leer el archivo de Excel
#     df = pd.read_excel(archivo, sheet_name='BD' )
#     # df.columns = df.iloc[1]
#     # df = df[2:]
#     #Elimina columna 
#     df = df.drop(columns=['COBRANZA'])
#     df = df.rename(columns={'Gestor': 'GESTOR'})
#     # try:
#     #     df.insert(0, 'Descripcion de Servicio', '')
#     # except ValueError:
#     #     print("La columna Descripcion de Servicio ")
    
#     # try:
#     #     df.insert(0, 'Correo 2', '')
#     # except ValueError:
#     #     print("Correo 2")

#     # Convertir la columna "GESTOR" a mayuscula
#     df['GESTOR'] = df['GESTOR'].str.lower()

#     # Filtrar por los registros donde "GESTOR" es igual a "AVAL" en mayuscula
#     df = df[df['GESTOR'] == 'aval']

#     # Renombrar las columnas
#     df = df.rename(columns={'IMPORTE': 'IMPORTE.0', 'FECHA': 'FECHA.0'})

#     df_final = pd.DataFrame()
    
     
#     # Obtener la última columna del dataframe
#     ultima_columna = df.columns[-1]
#     #Agarra todos los valores desde => . hacia la derecha
#     ultimo_numero = ultima_columna.split(".")[-1]
#     # print(df_final)
#     # Sumar un número más a cada uno de los valores
#     resultado = int(ultimo_numero) + 1


#     for i in range(0, resultado):
#         df_temp = df[['TipoDocumento', 'NumeroDocumento', 'N° Boleta ','GESTOR', 'GESTOR', 'Sede', 'FechaDocumento', 'FechaVencimiento', 'Año deuda',
#     'ClienteNombre', 'ClienteRUC', 'TipoVenta', 'Documento', 'FormadePago', 'MonedaDocumento', 'MontoTotal',
#     'MontoPagado', 'MontoPendiente', 'NombreCompleto', 'Criteria', 'UNIDAD', 'Teléfono 1', 'Teléfono 2',
#     'Correo 1 ', 'Correo 2', 'Tipo Documento Identidad', 'NumeroDocumentoIdentidad1', 'Descripcion de Servicio','GESTOR','GESTOR','GESTOR','GESTOR',
#     f'IMPORTE.{i}', f'FECHA.{i}']]
#         df_temp.columns = ['TIPO', 'NUMERO_DOCUMENTO', 'BOLETA', 'GESTOR', 'BUCKET', 'SEDE', 'FECHA_DOC', 'FECHA_VEN', 'ANIO_DEUDA', 
#         'CLIENTE_NOM', 'CLIENTE_RUC', 'TIPO_VENTA', 'CODIGO_ALUMNO__RUC', 'FORMA_PAGO', 'MONEDA_DOC', 'MONTO_TOTAL', 
#         'MONTO_PAGADO', 'SALDO', 'NOMBRE_COMPLETO', 'CRITERIA', 'UNIDAD', 'TELEFONO_CASA2', 'CELULAR2',
#         'CORREO', 'CORREO2', 'TIPO_DOCUMENTO_IDENTIDAD', 'NUMERODOCUMENTOIDENTIDAD', 'DESCRIPCION_DE_SERVICIO', 'PERIODO', 'CICLO', 'PROMEDIO', 'PORCENT_CONDONACION', 'IMPORTE_PAGO', 'FECHA_PAGO']
#         df_final = pd.concat([df_final, df_temp], axis=0, ignore_index=True)

#     df_final = df_final.dropna(subset=['IMPORTE_PAGO'])

#     #Poner en blanco
#     df_final['BUCKET'] = pd.np.nan
#     df_final['PORCENT_CONDONACION'] = pd.np.nan
#     df_final['PROMEDIO'] = pd.np.nan
#     df_final['CICLO'] = pd.np.nan
#     df_final['PERIODO'] = pd.np.nan
    
#     #Modifica fecha, para completar
#     def convertir_fecha(fecha):
#         try:
#             return fecha.strftime('%d/%m/%Y')
#         except:
#             return fecha
#     df_final['FECHA_DOC'] = df_final['FECHA_DOC'].apply(convertir_fecha)
#     # Convert the 'FECHA_DOC' column to a string data type
#     df_final['FECHA_DOC'] = df_final['FECHA_DOC'].astype(str)
#     mask = df_final['FECHA_DOC'].str.endswith('/202')
#     filas = df_final[mask].index
#     df_final.loc[filas, 'FECHA_DOC'] = df_final.loc[filas, 'FECHA_DOC'].apply(lambda x: x + '2') 
#     df_final['FECHA_DOC'] = pd.to_datetime(df_final['FECHA_DOC'], format='%d/%m/%Y')

#     #Regresa gestor a capitalize
#     df_final['GESTOR'] = df_final['GESTOR'].str.title()
    
#     # print(df_final)
#     #df_final.to_excel("nombre_del_archivo_modificado.xlsx", index=False)

#     return df_final
 
# def tabla_activa(archivo):
#     # Leer el archivo de Excel
#     df = pd.read_excel(archivo, sheet_name='Base de datos', header=1)
    
#     if 'FechaDocum' in df.columns and 'NumeroDocumentoIdentidad' in df.columns:
#         df = df.rename(columns={
#             'FechaDocum': 'FechaDocumento',
#             'NumeroDocumentoIdentidad': 'NumeroDocumentoIdentidad1'
#     })
    
#     #Elimina columna 
#     df = df.drop(columns=['COBRANZA'])
#     df = df.drop(columns=['Situacion academica'])
#     df = df.rename(columns={'Gestor': 'GESTOR'})
    
#     if 'Descripcion de Servicio' not in df.columns:
#         df.insert(0, 'Descripcion de Servicio', '')
#     if 'Correo 2' not in df.columns:
#         df.insert(0, 'Correo 2', '')

#     # Convertir la columna "GESTOR" a mayuscula
#     df['GESTOR'] = df['GESTOR'].str.lower()

#     # Filtrar por los registros donde "GESTOR" es igual a "AVAL" en mayuscula
#     df = df[df['GESTOR'] == 'aval']

#     # Renombrar las columnas
#     df = df.rename(columns={'IMPORTE': 'IMPORTE.0', 'FECHA': 'FECHA.0'})

#     df_final = pd.DataFrame()
    
     
#     # Obtener la última columna del dataframe
#     ultima_columna = df.columns[-1]
#     #Agarra todos los valores desde => . hacia la derecha
#     ultimo_numero = ultima_columna.split(".")[-1]

#     # Sumar un número más a cada uno de los valores
#     resultado = int(ultimo_numero) + 1


#     for i in range(0, resultado):
#         df_temp = df[['TipoDocumento', 'NumeroDocumento', 'N° Boleta ','GESTOR', 'GESTOR', 'Sede', 'FechaDocumento', 'FechaVencimiento', 'Año deuda',
#     'ClienteNombre', 'ClienteRUC', 'TipoVenta', 'Documento', 'FormadePago', 'MonedaDocumento', 'MontoTotal',
#     'MontoPagado', 'MontoPendiente', 'NombreCompleto', 'Criteria', 'UNIDAD', 'Teléfono 1', 'Teléfono 2',
#     'Correo 1 ', 'Correo 2', 'Tipo Documento Identidad', 'NumeroDocumentoIdentidad1', 'Descripcion de Servicio','GESTOR','GESTOR','GESTOR','GESTOR',
#     f'IMPORTE.{i}', f'FECHA.{i}']]
#         df_temp.columns = ['TIPO', 'NUMERO_DOCUMENTO', 'BOLETA', 'GESTOR', 'BUCKET', 'SEDE', 'FECHA_DOC', 'FECHA_VEN', 'ANIO_DEUDA', 
#         'CLIENTE_NOM', 'CLIENTE_RUC', 'TIPO_VENTA', 'CODIGO_ALUMNO__RUC', 'FORMA_PAGO', 'MONEDA_DOC', 'MONTO_TOTAL', 
#         'MONTO_PAGADO', 'SALDO', 'NOMBRE_COMPLETO', 'CRITERIA', 'UNIDAD', 'TELEFONO_CASA2', 'CELULAR2',
#         'CORREO', 'CORREO2', 'TIPO_DOCUMENTO_IDENTIDAD', 'NUMERODOCUMENTOIDENTIDAD', 'DESCRIPCION_DE_SERVICIO', 'PERIODO', 'CICLO', 'PROMEDIO', 'PORCENT_CONDONACION', 'IMPORTE_PAGO', 'FECHA_PAGO']
#         df_final = pd.concat([df_final, df_temp], axis=0, ignore_index=True)

#     df_final = df_final.dropna(subset=['IMPORTE_PAGO'])

#     #Poner en blanco
#     df_final['BUCKET'] = pd.np.nan
#     df_final['PORCENT_CONDONACION'] = pd.np.nan
#     df_final['PROMEDIO'] = pd.np.nan
#     df_final['CICLO'] = pd.np.nan
#     df_final['PERIODO'] = pd.np.nan
    
        
#     df_final['FECHA_DOC'] = df_final['FECHA_DOC'].apply(convertir_fecha)
#     # Convert the 'FECHA_DOC' column to a string data type
#     df_final['FECHA_DOC'] = df_final['FECHA_DOC'].astype(str)
#     mask = df_final['FECHA_DOC'].str.endswith('/202')
#     filas = df_final[mask].index
#     df_final.loc[filas, 'FECHA_DOC'] = df_final.loc[filas, 'FECHA_DOC'].apply(lambda x: x + '2') 
#     df_final['FECHA_DOC'] = pd.to_datetime(df_final['FECHA_DOC'], format='%d/%m/%Y')

#     #Regresa gestor a capitalize
#     df_final['GESTOR'] = df_final['GESTOR'].str.title()
    
#     df_final = convertir_a_float(df_final, 'MONTO_TOTAL')
#     df_final = convertir_a_float(df_final, 'MONTO_PAGADO')
#     df_final = convertir_a_float(df_final, 'SALDO')
    

#     return df_final



