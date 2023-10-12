import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

def convertir_a_float(df, columna):
    df[columna] = df[columna].apply(lambda x: float(x) if x != '' else 0)
    return df

def tabla2(archivo):
    # Leer el archivo de Excel
    wb = openpyxl.load_workbook(archivo)
    ws = wb['Base de datos']
    data = ws.values
    columns = next(data)[1:]
    df = pd.DataFrame(data, columns=columns)

    if 'IMPORTE' not in df.columns:
        print('Nell')
        return None
    else:
        if 'N° Boleta ' not in df.columns:
            df = df.rename(columns={'N° Boleta': 'N° Boleta '})

        # Elimina columna
        df = df.drop(columns=['COBRANZA'])
        df = df.rename(columns={'Gestor': 'GESTOR'})
        # Convertir la columna "GESTOR" a mayuscula
        df['GESTOR'] = df['GESTOR'].str.lower()

        # Filtrar por los registros donde "GESTOR" es igual a "AVAL" en mayuscula
        df = df[df['GESTOR'] == 'aval']

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
        # Agarra todos los valores desde => . hacia la derecha
        ultimo_numero = ultima_columna.split(".")[-1]
        # Sumar un número más a cada uno de los valores
        resultado = int(ultimo_numero) + 1

        # Resto del código...
        for i in range(0, resultado):
            df_temp = df[['TipoDocumento', 'NumeroDocumento', 'N° Boleta ','GESTOR', 'GESTOR', 'S', 'FechaDocumento', 'FechaVencimiento', 'Año deuda',
                    'ClienteNombre', 'ClienteRUC', 'TipoVenta', 'Documento', 'FormadePago', 'MonedaDocumento', 'MontoTotal',
                    'MontoPagado', 'MontoPendiente', 'NombreCompleto', 'Criteria', 'UNIDAD', 'Teléfono 1', 'Teléfono 2',
                    'Correo 1 ', 'Correo 2', 'Tipo Documento Identidad', 'NumeroDocumentoIdentidad1', 'Descripcion de Servicio','GESTOR','GESTOR','GESTOR','GESTOR',
                    f'IMPORTE.{i}', f'FECHA.{i}']]
            df_temp.columns = ['TIPO', 'NUMERO_DOCUMENTO', 'BOLETA', 'GESTOR', 'BUCKET', 'SE', 'FECHA_DOC', 'FECHA_VEN', 'ANIO_DEUDA', 
                    'CLIENTE_NOM', 'CLIENTE_RUC', 'TIPO_VENTA', 'CODIGO_ALUMNO__RUC', 'FORMA_PAGO', 'MONEDA_DOC','MONTO_TOTAL', 
                    'MONTO_PAGADO', 'SALDO', 'NOMBRE_COMPLETO', 'CRITERIA', 'UNIDAD', 'TELEFONO_CASA2', 'CELULAR2',
                    'CORREO', 'REO2', 'TIPO_DOCUMENTO_IDENTIDAD', 'NUMERODOCUMENTOIDENTIDAD', 'DESCRIPCION_DE_SERVICIO', 'PERIODO', 'CICLO', 'PROMEDIO', 'PORCENT_CONDONACION', 'IMPORTE_PAGO', 'FECHA_PAGO']
            df_final = pd.concat([df_final, df_temp], axis=0, ignore_index=True)

        df_final = df_final.dropna(subset=['IMPORTE_PAGO'])

        # Poner en blanco
        df_final['BUCKET'] = pd.np.nan
        df_final['PORCENT_CONDONACION'] = pd.np.nan
        df_final['PROMEDIO'] = pd.np.nan
        df_final['CICLO'] = pd.np.nan
        df_final['PERIODO'] = pd.np.nan

        # Modifica fecha, para completar        
        def convertir_fecha(fecha):
            try:
                return fecha.strftime('%d/%m/%Y')
            except:
                return fecha
            
        df_final['FECHA_DOC'] = df_final['FECHA_DOC'].apply(convertir_fecha)
        # Convert the 'FECHA_DOC' column to a string data type
        df_final['FECHA_DOC'] = df_final['FECHA_DOC'].astype(str)
        mask = df_final['FECHA_DOC'].str.endswith('/202')
        filas = df_final[mask].index
        df_final.loc[filas, 'FECHA_DOC'] = df_final.loc[filas, 'FECHA_DOC'].apply(lambda x: x + '2') 
        df_final['FECHA_DOC'] = pd.to_datetime(df_final['FECHA_DOC'], format='%d/%m/%Y')

        # Regresa gestor a capitalize
        df_final['GESTOR'] = df_final['GESTOR'].str.title()
        df_final = convertir_a_float(df_final, 'MONTO_TOTAL')
        df_final = convertir_a_float(df_final, 'MONTO_PAGADO')
        df_final = convertir_a_float(df_final, 'SALDO')

        return df_final

 