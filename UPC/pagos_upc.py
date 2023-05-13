import pandas as pd
from datetime import datetime
import os
import shutil

fechaa=datetime.now().strftime('%d.%m.%Y')
archivo1='CANCELADOS AVAL '+fechaa+'.xlsx'
# archivo1='CANCELADOS AVAL 04.05.2023.xlsx'
# Cargar archivo Excel y seleccionar hoja "Base1"
df = pd.read_excel(archivo1, sheet_name='Hoja1')

df['TIPO_DOCT'] = df['TIPO Y NUMERO DE DOCUMENTO'].str.slice(stop=2)
df['NUM_DOCT'] = df['TIPO Y NUMERO DE DOCUMENTO'].str.slice(start=2)
fecha_formateada = datetime.now().strftime('%d/%m/%Y')
df['FECHA_PAGO'] = datetime.strptime(fecha_formateada, '%d/%m/%Y')
# Convertir la columna "FECHA_EMISION" a formato "dd/mm/YYYY"
# df['FECHA_EMISION'] = pd.to_datetime(df['FECHA_EMISION']).dt.strftime('%d/%m/%Y')
# df['FECHA_VENCIMIENTO'] = pd.to_datetime(df['FECHA_VENCIMIENTO']).dt.strftime('%d/%m/%Y')
df['RUC'] = ''
df['MORA'] = ''
df['CIERRE_MES'] = ''
df['OBSERVACIONES'] = ''
df['TC'] = ''
df['CONSIDERADO'] = ''

 # Cambiar valores de MONEDA por "LO" cuando su valor sea "PEN"
df.loc[df['MONEDA'] == 'PEN', 'MONEDA'] = 'LO'

new_cols = [
'UNIDAD DE NEGOCIO','CODIGO ALUMNO','TIPO DE DOCUMENTO DE IDENTIDAD',
'NUMERO DE DOCUMENTO DE IDENTIDAD','RUC','RAZON SOCIAL','APELLIDOS Y NOMBRES DEL ALUMNO',
'TIPO_DOCT','NUM_DOCT','TIPO Y NUMERO DE DOCUMENTO',
'FECHA_EMISION','FECHA_VENCIMIENTO','DIAS DE ANTIQUAMIENTO','MONEDA','MONTO_ORIGINAL',
'DEUDA','FECHA_PAGO', 'MORA','CIERRE_MES', 'OBSERVACIONES', 'TC', 'CONSIDERADO']
df = df[new_cols]
 
df.columns=['UNIDAD_DE_NEGOCIO', 'CODIGO_ALUMNO', 'TIPO_DE_DOCUMENTO_DE_IDENTIDAD',
    'NUMERO_DE_DOCUMENTO_DE_IDENTIDAD', 'RUC', 'RAZON_SOCIAL',
    'APELLIDOS_Y_NOMBRES_DEL_ALUMNO', 'TIPO_DE_DOCUMENTO_DE_PAGO',
    'NUMERO_DE_DOCUMENTO_DE_PAGO', 'TIPO_Y_NUMERO_DE_DOCUMENTO',
    'FECHA_EMISION', 'FECHA_VENCIMIENTO', 'DIAS_DE_ANTIQUAMIENTO',
    'MONEDA', 'IMPORTE', 'IMPORTE_SOLES', 'FECHA_PAGO', 'MORA',
    'CIERRE_MES', 'OBSERVACIONES', 'TC', 'CONSIDERADO']


# Obtener la fecha actual en formato dd_mm
fecha_actual = datetime.now().strftime('%d_%m')

# Crear la ruta de la carpeta en el escritorio con la fecha actual
# ruta_carpeta = os.path.join(os.path.expanduser('~'), 'Desktop',  fecha_actual+'p cibert')
# Este define la ruta si tienes onedrive, el anterior es si no lo tiene
ruta_carpeta = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Escritorio',  fecha_actual+'p UPC')
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)

ruta_archivo = os.path.join(ruta_carpeta, fecha_actual+' Pagos UPC.xlsx')

df.to_excel(ruta_archivo, index=False)

shutil.move(archivo1,ruta_carpeta)