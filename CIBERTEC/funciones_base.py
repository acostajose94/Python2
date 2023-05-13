import pandas as pd


def tabla_base(archivo):
    
    xls = pd.ExcelFile(archivo)
    if 'BD' in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name='BD', header=1)
    elif 'BD ' in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name='BD ', header=1)
    elif 'Base de datos' in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name='Base de datos', header=1)
    else:
        print("No se encontró la hoja 'BD' o 'BD ' en el archivo de Excel.")
        return None
    
    df = df.rename(columns={'Gestor': 'GESTOR'})
    df['GESTOR'] = df['GESTOR'].str.lower()
    # Filtrar por los registros donde "GESTOR" es igual a "AVAL" en mayuscula
    df = df[df['GESTOR'] == 'aval']
    
    if 'Situacion academica'  in df.columns:
        df['Situacion academica'] = df['Situacion academica'].str.lower()
        df = df[df['Situacion academica'] == 'activo']
    
    df.insert(0, column='PERIODO', value='')
    df.insert(0, column='CICLO', value='')
    df.insert(0, column='PROMEDIO', value='')
    df.insert(0, column='PORC_CONDONACION', value='')
    df.insert(0, column='CONDONACION_ADICIONAL', value='')
    df.insert(0, column='DSCTO_MATRICULA', value='')
    df.insert(0, column='ESTADO', value='')
    df.insert(0, column='TELEFONO_CASA2', value='')
    df.insert(0, column='TELEFONO_CASA', value='')
    df.insert(0, column='CELULAR2', value='')
    df.insert(0, column='CORREO2', value='')
    df.insert(0, column='vacio', value='')
    
    if 'Descripcion de Servicio' not in df.columns:
        df.insert(0, 'Descripcion de Servicio', '')
    if 'Correo 2' not in df.columns:
        df.insert(0, 'Correo 2', '')
    if 'Correo 1' not in df.columns:
        df = df.rename(columns={'Correo 1 ': 'Correo 1'})
    if 'N° Boleta ' not in df.columns:
        df = df.rename(columns={'N° Boleta': 'N° Boleta '})
    if 'FechaDocum' in df.columns:
        df = df.rename(columns={'FechaDocum': 'FechaDocumento'})
    if 'NumeroDocumentoIdentidad' in df.columns:
        df = df.rename(columns={'NumeroDocumentoIdentidad': 'NumeroDocumentoIdentidad1'})
 
    # Cambiar el orden de las columnas
    df = df[['TipoDocumento', 'NumeroDocumento', 'N° Boleta ', 'GESTOR', 'vacio', 'Sede', 'FechaDocumento',
         'FechaVencimiento', 'Año deuda', 'ClienteNombre', 'ClienteRUC', 'TipoVenta', 'Documento', 
         'FormadePago', 'MonedaDocumento', 'MontoTotal', 'MontoPagado', 'MontoPendiente', 
         'NombreCompleto', 'Criteria', 'UNIDAD', 'Teléfono 1', 'Teléfono 2', 'Correo 1', 'Correo 2', 
         'Tipo Documento Identidad', 'NumeroDocumentoIdentidad1', 'Descripcion de Servicio', 
         'PERIODO', 'CICLO', 'PROMEDIO', 'PORC_CONDONACION', 'CONDONACION_ADICIONAL', 
         'DSCTO_MATRICULA', 'ESTADO', 'TELEFONO_CASA2', 'TELEFONO_CASA', 'CELULAR2', 'CORREO2']]

    
    # lista con los nuevos nombres de las columnas
    new_cols = ['TIPO', 'NUMERO_DOCUMENTO', 'BOLETA', 'GESTOR', 'BUCKET', 'SEDE', 'FECHA_DOC', 'FECHA_VEN', 'AÑO_DEUDA', 'CLIENTENOMBRE', 'CLIENTERUC', 'TIPO_VENTA', 'CODIGO_ALUMNO__RUC', 'FORMADEPAGO', 'MONEDA_DOC', 'MONTO_TOTAL', 'MONTO_PAGADO', 'SALDO', 'NOMBRE_COMPLETO', 'CRITERIA', 'UNIDAD', 'TELEFONOS', 'CELULAR', 'CORREO', 'CORREO_ELECTRONICO', 'TIPO_DOCUMENTO_IDENTIDAD', 'NUMERODOCUMENTOIDENTIDAD', 'DESCRIPCION_DE_SERVICIO', 'PERIODO', 'CICLO', 'PROMEDIO', 'PORC_CONDONACION', 'CONDONACION_ADICIONAL', 'DSCTO_MATRICULA', 'ESTADO', 'TELEFONO_CASA2', 'TELEFONO_CASA', 'CELULAR2', 'CORREO2']

    # Renombrar las columnas
    df.columns = new_cols
    df_final = df

    df_final['FECHA_DOC'] = df_final['FECHA_DOC'].apply(convertir_fecha)
    df_final['FECHA_DOC'] = df_final['FECHA_DOC'].astype(str)
    mask = df_final['FECHA_DOC'].str.endswith('/202')
    filas = df_final[mask].index
    df_final.loc[filas, 'FECHA_DOC'] = df_final.loc[filas, 'FECHA_DOC'].apply(lambda x: x + '2') 
    df_final['FECHA_DOC'] = pd.to_datetime(df_final['FECHA_DOC'], format='%d/%m/%Y')
    
    df_final = convertir_a_float(df_final, 'MONTO_TOTAL')
    df_final = convertir_a_float(df_final, 'MONTO_PAGADO')
    
    return df_final
    
    

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
  