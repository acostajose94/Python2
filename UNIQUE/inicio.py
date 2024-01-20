import os
import glob
from openpyxl import Workbook

# Carpeta donde se encuentran los archivos .txt
folder = "ruta_de_la_carpeta"

# Carpeta donde se guardará el archivo .xlsx
save_folder = "ruta_de_la_carpeta_destino"

# Crear un nuevo archivo de trabajo
workbook = Workbook()

# Agregar un nuevo hoja de cálculo
worksheet = workbook.active

# Enumerar todos los archivos .txt en la carpeta
txt_files = glob.glob(os.path.join(folder, "*.txt"))

# Unificar todos los archivos .txt en una carpeta
for file in txt_files:
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            # Agregar cada línea del archivo .txt a una celda en la hoja de cálculo
            worksheet.append([line.strip()])

# Guardar el archivo de trabajo como un archivo .xlsx en la carpeta destino
workbook.save(os.path.join(save_folder, "result.xlsx"))