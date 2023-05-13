import pandas as pd

# Cargar archivo Excel y seleccionar hoja "Base1"
df = pd.read_excel('CARTERA TOTAL TERCERIZADA AVAL 05.04.2023.xlsx', sheet_name='Hoja2')

  
# agregar columnas vacías en posiciones específicas
df.insert(4, 'columna4', '')
df.insert(19, 'columna19', '')
df.insert(20, 'columna20', '')
df.insert(21, 'columna21', '')
df['TIPO_DOCT'] = df['TIPO Y NUMERO DE DOCUMENTO'].str.slice(stop=2)
df['NUM_DOCT'] = df['TIPO Y NUMERO DE DOCUMENTO'].str.slice(start=2)
df['ANIO_VENCIMIENTO'] = df['FECHA_VENCIMIENTO'].dt.year.astype(str)
df['CXC'] = df['TIPO Y NUMERO DE DOCUMENTO']
df['TELEFONO'] = ''
df['TELEFONO2'] = ''
df['CORREO'] = ''
df['CORREO2'] = ''

#Reordenar contenido
new_cols = [
    'UNIDAD DE NEGOCIO', 'CODIGO ALUMNO', 'TIPO DE DOCUMENTO DE IDENTIDAD', 'NUMERO DE DOCUMENTO DE IDENTIDAD',
    'columna4','RAZON SOCIAL', 'APELLIDOS Y NOMBRES DEL ALUMNO','TIPO_DOCT','NUM_DOCT', 'TIPO Y NUMERO DE DOCUMENTO', 'FECHA_EMISION', 'FECHA_VENCIMIENTO',
    'DIAS DE ANTIQUAMIENTO', 'MONEDA', 'MONTO_ORIGINAL','CXC','ANIO_VENCIMIENTO', 'DEUDA', 'EMPRESA_EXTERNA','columna19', 'columna20','columna21', 'FACULTAD/CARRERA', 'CAMPUS',
    'NOMBRE_CARTERA','TELEFONO','TEEFONO2','CORREO','CORREO2'
]
df = df[new_cols]

#cambiar cabecera 
df = df.columns['UNIDAD_DE_NEGOCIO','CODIGO_ALUMNO','TIPO_DE_DOCUMENTO_DE_IDENTIDAD','NUMERO_DE_DOCUMENTO_DE_IDENTIDAD','RUC','RAZON_SOCIAL',
'APELLIDOS_Y_NOMBRES_DEL_ALUMNO','TIPO_DE_DOCUMENTO_DE_PAGO','NUMERO_DE_DOCUMENTO_DE_PAGO','TIPO_Y_NUMERO_DE_DOCUMENTO',
'FECHA_EMISION','FECHA_VENCIMIENTO','DIAS_DE_ANTIQUAMIENTO','MONEDA','IMPORTE','CXC','ANIOS','SOLES','ESTATUS','SENTINEL',
'INFOCORP','DESCRIPCION','CARRERA','CAMPUS','CAMPANNA','TELEFONO','TEEFONO2','CORREO','CORREO2'
]

# guardar en un archivo de Excel
df.to_excel('nombre_del_archivo_resultante.xlsx', index=False)
