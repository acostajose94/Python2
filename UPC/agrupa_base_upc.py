import pandas as pd

# Cargar archivo Excel y seleccionar hoja "Base1"
df = pd.read_excel('CARTERA TOTAL TERCERIZADA AVAL 05.04.2023.xlsx', sheet_name='Hoja1')
df2 = pd.read_excel('DATOS DE CONTACTO AVAL 05.04.23.xlsx', sheet_name='Hoja1')
  
# agregar columnas vacías en posiciones específicas
df.insert(0, column='columna4', value='')
df.insert(0, column='columna19', value='')
df.insert(0, column='columna20', value='')
df.insert(0, column='columna21', value='')
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
    'NOMBRE_CARTERA','TELEFONO','TELEFONO2','CORREO','CORREO2'
]
df = df[new_cols]

#cambiar cabecera 
df.columns = ['UNIDAD_DE_NEGOCIO','CODIGO_ALUMNO','TIPO_DE_DOCUMENTO_DE_IDENTIDAD','NUMERO_DE_DOCUMENTO_DE_IDENTIDAD','RUC','RAZON_SOCIAL',              'APELLIDOS_Y_NOMBRES_DEL_ALUMNO','TIPO_DE_DOCUMENTO_DE_PAGO','NUMERO_DE_DOCUMENTO_DE_PAGO','TIPO_Y_NUMERO_DE_DOCUMENTO',              'FECHA_EMISION','FECHA_VENCIMIENTO','DIAS_DE_ANTIQUAMIENTO','MONEDA','IMPORTE','CXC','ANIOS','SOLES','ESTATUS','SENTINEL',              'INFOCORP','DESCRIPCION','CARRERA','CAMPUS','CAMPANNA','TELEFONO','TELEFONO2','CORREO','CORREO2']


telefono_dict = df2.set_index('COD_ALUMNO')['TELEFONO_1'].to_dict()
# Actualizar los valores de la columna TELEFONO en el DataFrame df utilizando el diccionario
df['TELEFONO'] = df['CODIGO_ALUMNO'].map(telefono_dict).fillna(df['TELEFONO'])

telefono_dict2 = df2.set_index('COD_ALUMNO')['TELEFONO_2'].to_dict()
# Actualizar los valores de la columna TELEFONO en el DataFrame df utilizando el diccionario
df['TELEFONO2'] = df['CODIGO_ALUMNO'].map(telefono_dict2).fillna(df['TELEFONO2'])

correo_dict = df2.set_index('COD_ALUMNO')['Mail_Institución'].to_dict()
# Actualizar los valores de la columna TELEFONO en el DataFrame df utilizando el diccionario
df['CORREO'] = df['CODIGO_ALUMNO'].map(telefono_dict2).fillna(df['CORREO2'])

correo_dict2 = df2.set_index('COD_ALUMNO')['Mail_Personal_1'].to_dict()
# Actualizar los valores de la columna TELEFONO en el DataFrame df utilizando el diccionario
df['CORREO2'] = df['CODIGO_ALUMNO'].map(telefono_dict2).fillna(df['CORREO2'])



# guardar en un archivo de Excel
df.to_excel('nombre_del_archivo_resultante.xlsx', index=False)
