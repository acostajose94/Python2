import openpyxl
from funciones_columna import *
# Reemplaza 'archivo.xlsx' con el nombre de tu archivo de Excel
archivo_excel = 'AVAL_TLS_PREGRADO VIGENTE al  180523.xlsx'

# Abre el archivo de Excel
workbook = openpyxl.load_workbook(archivo_excel)
sheet = workbook.active

formato_texto(sheet,2)
formato_texto(sheet,3)
formato_texto(sheet,8)
formato_texto(sheet,9)
formato_numero(sheet,15)
formato_fecha(sheet,21)
formato_fecha(sheet,20)
formato_texto(sheet,23)
formato_fecha(sheet,24)
formato_texto(sheet,27)
formato_texto(sheet,28)
formato_fecha(sheet,29)
formato_texto(sheet,35)
formato_texto(sheet,37)
# Agregar columna en blanco en la tercera posición entre EMPLID y CODIGO
sheet.insert_cols(3)

# Agregar dos columnas en blanco en la tercera posición entre NOMBRES y DIRECCION
sheet.insert_cols(6)
sheet.insert_cols(6)

# Verificar si la columna "KOMODO" existe
columna_komodo = None
for cell in sheet[1]:
    if cell.value == "KOMODO":
        columna_komodo = cell.column_letter
        break
# Eliminar la columna "KOMODO" si existe
if columna_komodo:
    sheet.delete_cols(sheet[columna_komodo][0].col_idx)
    
# Cambiar la cabecera
cabecera_nueva = [
    'SOCIEDAD', 'EMPLID', 'UNICO', 'CODIGO', 'APELLIDOS', 'NOMBRES', 'TP_DOC_ID', 'DOC_ID',
    'DIRECCION', 'DISTRITO', 'TELEFONO', 'CELULAR', 'EMAIL', 'PROGRAMA', 'CURSO', 'PERIODO',
    'DESCRIPCION', 'SALDO', 'MONEDA', 'STATUS_CARRERA', 'MASIVA', 'NUM_MASIVA', 'FECHA_EMISION',
    'FECHA_VENCIMIENTO', 'NOTA_CRED', 'ID_FCRONOGRAMA', 'FECHA_FIN_PROGRANMA', 'CICLO',
    'RAZON_SOCIAL', 'RUC', 'PHONE_EMPRESA', 'FECHA_DE_CORTE', 'DESCR', 'PAL_CLAVE_2', 'REF',
    'REF_FECHA', 'REF_COMENTARIOS', 'ID_ORG_EXT', 'CANJE', 'SESION', 'TIPO_PROGRAMA', 'ASESOR'
]
 
# Asignar los valores de la nueva cabecera
for col_idx, valor in enumerate(cabecera_nueva, start=1):
    sheet.cell(row=1, column=col_idx, value=valor)


# Reemplaza 'archivo.xlsx' con el nombre de tu archivo de Excel
archivo_excel = 'archivo.xlsx'
# Guardar los cambios en el archivo de Excel
workbook.save(archivo_excel)
