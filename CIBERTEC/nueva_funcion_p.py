import pandas as pd
import os
from datetime import datetime
from dateutil.parser import parse
import re
def procesar_archivo_excel(excel_file):
    # Cargar el archivo de Excel
    xls = pd.ExcelFile(excel_file)

    # Crear una lista para almacenar los DataFrames procesados de cada hoja
    dfs_procesados = []

    # Recorrer cada hoja del archivo Excel
    for sheet_name in xls.sheet_names:
         
        df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)

        # Encontrar la fila que contiene la cabecera
        header_row = None
        for index, row in df.iterrows():
            if 'COD_ALUMNO' in str(row.values):
                header_row = index
                break

        if header_row is not None:
            # Volver a cargar el archivo Excel con la cabecera en la fila detectada
            df = pd.read_excel(excel_file, sheet_name=sheet_name, header=header_row)
        else:
            print(f"No se encontró la cabecera en la hoja {sheet_name}.")
            break

        # Convertir la columna 'Gestor' a minúsculas
        df['Gestor'] = df['Gestor'].str.lower()
        # Convertir todos los valores a cadenas y luego a minúsculas
        # df['Gestor'] = df['Gestor'].astype(str).str.lower()

        # Filtrar por 'Gestor' que contenga 'aval'
        df_filtrado = df[df['Gestor'].str.contains('aval', case=False)]

        # Filtrar por registros con monto de pago
        df_filtrado_monto = df_filtrado[df_filtrado['MONTO_PAGO'].notnull()]

        # Verificar si el DataFrame resultante está vacío
        # if df_filtrado_monto.empty:
        #     return None

        # Agregar una columna vacía llamada 'columna_vacia'
        #df_filtrado_monto['columna_vacia'] = ''
        df_filtrado_monto['columna_vacia'] = pd.Series(dtype=object)
        # df_filtrado_monto = df_filtrado_monto.assign(columna_vacia='')

        
        # Reordenar las columnas según el formato deseado
        column_order = ['DOC_PENDIENTE', 'DOC_PENDIENTE', 'DOC_PENDIENTE', 'Gestor', 'columna_vacia', 'columna_vacia', 'columna_vacia',
                        'columna_vacia', 'columna_vacia', 'columna_vacia', 'columna_vacia', 'columna_vacia',
                        'COD_ALUMNO', 'columna_vacia', 'MONEDA', 'columna_vacia','columna_vacia',
                        'columna_vacia', 'columna_vacia', 'columna_vacia', 'columna_vacia', 'columna_vacia',
                        'columna_vacia', 'columna_vacia', 'columna_vacia', 'columna_vacia', 'columna_vacia',
                        'columna_vacia', 'columna_vacia', 'columna_vacia', 'columna_vacia', 'columna_vacia',
                        'MONTO_PAGO', 'FECHA_COBRANZA','BANCO','ID_DEPOSITO']
        df_filtrado_monto = df_filtrado_monto.reindex(columns=column_order)

        # Cambiar los nombres de las columnas
        new_column_names = ['TIPO', 'NUMERO_DOCUMENTO', 'BOLETA', 'GESTOR', 'BUCKET', 'SEDE', 'FECHA_DOC',
                            'FECHA_VEN', 'ANIO_DEUDA', 'CLIENTE_NOM', 'CLIENTE_RUC', 'TIPO_VENTA',
                            'CODIGO_ALUMNO__RUC', 'FORMA_PAGO', 'MONEDA_DOC', 'MONTO_TOTAL', 'MONTO_PAGADO',
                            'SALDO', 'NOMBRE_COMPLETO', 'CRITERIA', 'UNIDAD', 'TELEFONO_CASA2',
                            'CELULAR2','CORREO', 'CORREO2', 'TIPO_DOCUMENTO_IDENTIDAD', 'NUMERODOCUMENTOIDENTIDAD',
                            'DESCRIPCION_DE_SERVICIO', 'PERIODO', 'CICLO', 'PROMEDIO', 'PORCENT_CONDONACION',
                            'IMPORTE_PAGO', 'FECHA_PAGO','BANCO','ID_DEPOSITO']
        df_filtrado_monto.columns = new_column_names

        # Convertir la columna 'TIPO' a tipo string
        df_filtrado_monto['TIPO'] = df_filtrado_monto['TIPO'].astype(str)
        # Cambiar los valores de 'TIPO'
        df_filtrado_monto['TIPO'] = df_filtrado_monto['TIPO'].str.slice(0, 2)

        # Convertir la columna 'NUMERO_DOCUMENTO' a tipo string
        df_filtrado_monto['NUMERO_DOCUMENTO'] = df_filtrado_monto['NUMERO_DOCUMENTO'].astype(str)
        # Cambiar los valores de 'NUMERO_DOCUMENTO'
        df_filtrado_monto['NUMERO_DOCUMENTO'] = df_filtrado_monto['NUMERO_DOCUMENTO'].str.slice(2)

        # Agregar el DataFrame procesado a la lista
        dfs_procesados.append(df_filtrado_monto)
        
    # Combinar todos los DataFrames procesados en uno solo
    df_resultado = pd.concat(dfs_procesados, ignore_index=True)
    # print(df_resultado['FECHA_PAGO'])
    # df_resultado['FECHA_PAGO'] = df_resultado['FECHA_PAGO'].astype(str)
    # mask = df_resultado['FECHA_PAGO'].str.endswith('/202')
    # filas = df_resultado[mask].index
    # df_resultado.loc[filas, 'FECHA_PAGO'] = df_resultado.loc[filas, 'FECHA_PAGO'].apply(lambda x: x + '3') 
        
    # def convertir_formato_fecha(fecha):
    #     patrones = [
    #             r'\d{2}/\d{2}/\d{4}',  # formato 'dd/mm/yyyy'
    #             r'\d{4}-\d{2}-\d{2}',  # formato 'yyyy-mm-dd'
    #     ]

    #     for patron in patrones:
    #             coincidencia = re.match(patron, fecha)
    #             if coincidencia:
    #                 fecha_match = coincidencia.group()
    #                 if '/' in fecha_match:
    #                     nueva_fecha = pd.to_datetime(fecha_match, format='%d/%m/%Y')
    #                 else:
    #                     nueva_fecha = pd.to_datetime(fecha_match, format='%Y-%m-%d')
    #                 return nueva_fecha.strftime('%d/%m/%Y')

    #     return fecha
            
    # df_resultado['FECHA_PAGO'] = df_resultado['FECHA_PAGO'].apply(convertir_formato_fecha)
    # df_resultado['FECHA_PAGO'] = pd.to_datetime(df_resultado['FECHA_PAGO'], format='%d/%m/%Y')
    
    print(df_resultado['FECHA_PAGO'])
    return df_resultado


def verifica_carpeta(fecha_actual,acti):
    ruta_carpeta=os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Escritorio',  fecha_actual+'p cibert '+acti)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    return ruta_carpeta
    
    

