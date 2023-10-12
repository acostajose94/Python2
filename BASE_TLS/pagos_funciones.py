import glob
import os
from openpyxl import load_workbook
from openpyxl.styles import numbers
import shutil

import zipfile
import rarfile


def eliminar_archivos_excel(ruta_actual):
     
    archivos = os.listdir(ruta_actual)
    
    for archivo in archivos:
        if archivo.endswith(".xlsx") or archivo.endswith(".xls"):
            archivo_path = os.path.join(ruta_actual, archivo)
            os.remove(archivo_path)
            print(f"Archivo eliminado: {archivo_path}")

def extraer_archivo_mas_reciente(ruta_actual):
 

    # Buscar archivos ZIP y RAR en la carpeta actual
    archivos_zip = glob.glob(os.path.join(ruta_actual, '*.zip'))
    archivos_rar = glob.glob(os.path.join(ruta_actual, '*.rar'))

    # Combinar y ordenar los archivos por fecha de modificación descendente
    archivos = sorted(archivos_zip + archivos_rar, key=os.path.getmtime, reverse=True)

    if archivos:
        archivo_mas_reciente = archivos[0]
        nombre_archivo, extension = os.path.splitext(archivo_mas_reciente)

        # Extraer archivo ZIP
        if extension == '.zip':
            with zipfile.ZipFile(archivo_mas_reciente, 'r') as archivo_zip:
                archivo_zip.extractall(ruta_actual)
                print(f'Se ha extraído el archivo ZIP más reciente: {archivo_mas_reciente}')

        # Extraer archivo RAR
        elif extension == '.rar':
            with rarfile.RarFile(archivo_mas_reciente, 'r') as archivo_rar:
                archivo_rar.extractall(ruta_actual)
                print(f'Se ha extraído el archivo RAR más reciente: {archivo_mas_reciente}')
        
        return archivo_mas_reciente

    else:
        print('No se encontraron archivos ZIP o RAR en la carpeta actual.')
   

def buscar_archivo_mas_reciente(directorio, palabra):
    # Buscar archivos que contengan la palabra
    archivos = glob.glob(os.path.join(directorio, f'*{palabra}*'))
    
    # Verificar si se encontraron archivos
    if not archivos:
        return None
    
    # Obtener el archivo más reciente
    archivo_mas_reciente = max(archivos, key=os.path.getmtime)
    
    return archivo_mas_reciente

def formato_texto(sheet, *columnas):
    if len(columnas) == 1 and isinstance(columnas[0], list):
        columnas = columnas[0]
    
    for columna in columnas:
        for row in sheet.iter_rows(min_row=2, min_col=columna, max_col=columna):
            cell = row[0]
            cell.number_format = '@'
            if isinstance(cell.value, (int, float)):
                cell.value = str(cell.value)
            
def formato_numero(sheet, *columnas):
    if len(columnas) == 1 and isinstance(columnas[0], list):
        columnas = columnas[0]
        
    for columna in columnas:
        for row in sheet.iter_rows(min_row=2, min_col=columna, max_col=columna):
            cell = row[0]
            valor = cell.value
            if valor is not None and isinstance(valor, str):
                valor = valor.replace(',', '.')
                cell.value = float(valor)
            cell.number_format = '0.00'

def formato_fecha(sheet, *columnas):
    if len(columnas) == 1 and isinstance(columnas[0], list):
        columnas = columnas[0]

    for columna in columnas:
        for row in sheet.iter_rows(min_row=2, min_col=columna, max_col=columna):
            for cell in row:
                # Verificar si el valor termina en "/202"
                valor = str(cell.value)
                if valor.endswith("/202"):
                    nuevo_valor = valor[:-4] + "2"
                    cell.value = nuevo_valor

                # Aplicar formato de fecha
                cell.number_format = numbers.FORMAT_DATE_XLSX14

def verificar_cabecera(sheet, cabecera_esperada):
    header_row = sheet[1]

    for cell, expected_value in zip(header_row, cabecera_esperada):
        if cell.value != expected_value:
            print(f"La cabecera esperada no coincide en la columna {cell.column}. Se esperaba '{expected_value}', pero se encontró '{cell.value}'.")
            return False

    return True

def define_carpeta(nombre_carpeta,fecha_actual):
    ruta_carpeta = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive', 'Escritorio', fecha_actual + nombre_carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    return ruta_carpeta

def buscar_posicion_por_nombre(sheet, nombre_columna):
    for columna in sheet.iter_cols(min_row=1, max_row=1):
        for celda in columna:
            if celda.value == nombre_columna:
                return celda.column  # Devuelve el número de columna
    return None  # Si no se encuentra, devuelve None


def pagos_certus(filename, cabecera_esperada, nueva_cabecera,fecha_actual):
    wb = load_workbook(filename)
    sheet = wb.active

    if verificar_cabecera(sheet, cabecera_esperada):
        print("La cabecera  correcta CERTUS")
        
        # Eliminar columnas F, G y H
        sheet.delete_cols(6, 3)
        formato_texto(sheet, 2, 3)
        formato_numero(sheet, 11, 12, 13, 14, 15, 16)
        formato_fecha(sheet, 7, 17, 18, 19, 20)

        for col_num, valor in enumerate(nueva_cabecera, 1):
            sheet.cell(row=1, column=col_num, value=valor)

        # Guardar los cambios en un nuevo archivo
        ruta_carpeta = define_carpeta('P CERTUS', fecha_actual)
        file_name = 'PAGOS_CERTUS' + fecha_actual + '.xlsx'
        new_filename = os.path.join(ruta_carpeta, file_name)
        wb.save(new_filename)

        # Abrir el archivo
        # os.startfile(new_filename)
        shutil.move(filename,ruta_carpeta)
        print("Certus Generado")
    else:
        print("La cabecera no es la esperada. Deteniendo la ejecución.")



def pagos_tls(filename,fecha_actual):
    wb = load_workbook(filename)
    sheet = wb.active
    
    formato_texto(sheet, 1)
    formato_numero(sheet,buscar_posicion_por_nombre(sheet,'Importe Pagado'))
    formato_fecha(sheet, buscar_posicion_por_nombre(sheet,'Fecha Pago'))
    
    ruta_carpeta = define_carpeta('P TLS', fecha_actual)
    file_name = 'PAGOS_TLS' + fecha_actual + '.xlsx'
    new_filename = os.path.join(ruta_carpeta, file_name)
    wb.save(new_filename)
    
    # Abrir el archivo
    ruta_v=r'V:\142. Ucal-Tls\\'
    shutil.copy(new_filename,ruta_v)
    # os.startfile(new_filename)
    shutil.move(filename,ruta_carpeta)
    print("TLS Generado")
    