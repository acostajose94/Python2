import pandas as pd
import os
def reordenar_columnas_y_guardar(nombre_archivo):
    # Leer el archivo Excel desde la hoja "Base de datos", omitiendo las dos primeras filas de encabezado
    df = pd.read_excel(nombre_archivo, sheet_name='Base de datos', header=1)

    # Filtrar la columna 'EMPRESA_EXTERNA', convertir a minúsculas y filtrar los valores que contengan 'aval'
    df['EMPRESA_EXTERNA'] = df['EMPRESA_EXTERNA'].str.lower()
    df = df[df['EMPRESA_EXTERNA'].str.contains('aval')]
    df['EMPRESA_EXTERNA'] = df['EMPRESA_EXTERNA'].str.capitalize()

    # Agregar una columna llamada 'esta_vacia' sin datos
    df['esta_vacia'] = ''

    # Definir el orden deseado de las cabeceras
    column_order = [
        'DOC_PENDIENTE', 'DOC_PENDIENTE', 'DOC_PENDIENTE', 'EMPRESA_EXTERNA', 'esta_vacia', 'CAMPUS', 'FEC_EMISION',
        'FEC_VENCIMIENTO', 'FEC_VENCIMIENTO', 'NOMBRE_COMPLETO', 'esta_vacia', 'esta_vacia', 'COD_ALUMNO', 'esta_vacia', 'MONEDA', 'MONTO_ORIGINAL','esta_vacia', 'DEUDA', 'NOMBRE_COMPLETO', 'esta_vacia', 'UNIDAD_NEGOCIO', 'esta_vacia', 'esta_vacia', 'esta_vacia', 'esta_vacia', 'TIPO_DOC_IDENTIDAD','NRO_DOC_IDENTIDAD', 'FACULTAD_CARRERA', 'PERIODO_ACADEMICO', 'esta_vacia', 'esta_vacia', 'esta_vacia', 'esta_vacia', 'esta_vacia', 'esta_vacia', 'esta_vacia', 'esta_vacia', 'esta_vacia', 'esta_vacia'
    ]

    # Obtener las cabeceras actuales
    current_headers = df.columns.tolist()

    # Reordenar las columnas basándose en los nombres de las cabeceras
    new_columns = [current_headers.index(col) for col in column_order if col in current_headers]
    df = df.iloc[:, new_columns]

    print(df)


    # Definir la nueva lista de nombres de columnas
    new_cols = [
                'TIPO', 'NUMERO_DOCUMENTO', 'BOLETA', 'GESTOR', 'BUCKET', 'SEDE', 'FECHA_DOC', 'FECHA_VEN', 'AÑO_DEUDA', 'CLIENTENOMBRE',
                'CLIENTERUC', 'TIPO_VENTA', 'CODIGO_ALUMNO__RUC', 'FORMADEPAGO', 'MONEDA_DOC', 'MONTO_TOTAL', 'MONTO_PAGADO', 'SALDO',
                'NOMBRE_COMPLETO', 'CRITERIA', 'UNIDAD', 'TELEFONOS', 'CELULAR', 'CORREO', 'CORREO_ELECTRONICO', 'TIPO_DOCUMENTO_IDENTIDAD',
                'NUMERODOCUMENTOIDENTIDAD', 'DESCRIPCION_DE_SERVICIO', 'PERIODO', 'CICLO', 'PROMEDIO', 'PORC_CONDONACION', 'CONDONACION_ADICIONAL',
                'DSCTO_MATRICULA', 'ESTADO', 'TELEFONO_CASA2', 'TELEFONO_CASA', 'CELULAR2', 'CORREO2'
                ]

    # Cambiar las cabeceras del DataFrame
    df.columns = new_cols

    return df



def verifica_carpeta(fecha_actual,acti):
    ruta_carpeta=os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Escritorio',  fecha_actual+'B cibert '+acti)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    return ruta_carpeta
    