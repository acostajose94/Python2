import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from b_funciones_NAT import *
from b_variables_NAT import *

archivo_reciente=extraer_archivo_mas_reciente()
archivos_excel=listar_excels()

ruta_carpeta=define_carpeta('B TLS',fecha_actual)

for archivo_excel in archivos_excel:
    # Abre el archivo de Excel
    workbook = openpyxl.load_workbook(archivo_excel)
    sheet = workbook['ASIGNACION']

    verificar_cabecera_completa(sheet, cabecera)
 
    columnas_a_eliminar = ['COLOR']
    eliminar_columnas_por_nombre(sheet, columnas_a_eliminar)
 
    # Agregar columna en blanco en la tercera posición entre EMPLID y CODIGO
    sheet.insert_cols(19)
    sheet.insert_cols(20)

   
    formato_texto(sheet,1,2,3,5,6,7)
    formato_numero(sheet, 25)
    formato_fecha(sheet, 8,9,10)

    # Asignar los valores de la nueva cabecera
    for col_idx, valor in enumerate(cabecera_nueva, start=1):
        sheet.cell(row=1, column=col_idx, value=valor)

    nombre_short=obtener_despues_de_pregrado(archivo_excel)
    ruta_base=os.path.join(ruta_carpeta, 'BASE TLS ' + nombre_short)
    workbook.save(ruta_base + '.xlsx')
    shutil.move(archivo_excel,ruta_carpeta)

    print(nombre_short)

    # print('Guardando')
    # guardar_archivo_mover('B TLS', workbook, hoy_carpeta,indice_inicio,archivo_excel,selec)
shutil.move(retira,ruta_carpeta)
print('Echo')

os.remove(archivo_reciente)