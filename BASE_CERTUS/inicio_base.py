import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from funciones import *
from variables import *

archivo_reciente=extraer_archivo_mas_reciente()
archivos_excel=listar_excels()
retira=obtener_excel_retira()
shutil.copy(retira, destino_retirar)
ruta_carpeta=define_carpeta('B CERTUS',fecha_actual)
print (ruta_carpeta)
for archivo_excel in archivos_excel:
    # Abre el archivo de Excel
    workbook = openpyxl.load_workbook(archivo_excel)
    sheet = workbook.active
    verificar_cabecera_completa(sheet, cabecera_esperada)
    sheet=insertar_columnas_vacias(sheet, nombre_columna, cantidad_columnas)
     
    elimina_tabulaciones(sheet)
    formato_texto(sheet, 1,2, 4, 7, 8, 9,10,16)
    formato_numero(sheet, 36,37,38,39,40,41,42,43,44)
    formato_fecha(sheet,25,27,31,32)
    # eliminar_columnas(sheet, 47, 48)
    # Después de formato_fecha(sheet, 25, 27, 31, 32)
    
    columnas_a_eliminar = ['COD. DUPL',	'EXT HBC']
    eliminar_columnas_por_nombre(sheet, columnas_a_eliminar)

        
    # Asignar los valores de la nueva cabecera
    for col_idx, valor in enumerate(nueva_cabecera, start=1):
        sheet.cell(row=1, column=col_idx, value=valor)

    posicion_cabecera = 49
    contenido_cabecera = 'AVAL 2023 PREGRADO'
    
    # Obtén la cantidad de filas en la hoja
    total_filas = sheet.max_row

    # Agregar 'AVAL 2023 PREGRADO' en todas las filas de la columna 49
    contenido_columna = 'AVAL 2023 PREGRADO'

    for fila in range(2, total_filas + 1):  # Comenzar desde la segunda fila hasta la última fila
        sheet.cell(row=fila, column=49, value=contenido_columna)
    
    corregir_valor_columna(sheet, 22, 'MA?ANA', 'MAÑANA')
    
    nombre_short=obtener_despues_de_pregrado(archivo_excel)
    ruta_base=os.path.join(ruta_carpeta, 'BASE CERTUS ' + nombre_short)
    workbook.save(ruta_base + '.xlsx')
    shutil.move(archivo_excel,ruta_carpeta)
    # guardar_archivo_mover('B CERTUS', workbook, fecha_actual,nombre_short,archivo_excel,retira)
    print(nombre_short)
shutil.move(retira,ruta_carpeta)
os.remove(archivo_reciente)