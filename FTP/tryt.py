import os
import datetime
hoy=datetime.datetime.now()
def renombrar_archivo(directorio,buscar,fecha_actual):
    fecha_actual=fecha_actual.strftime('%Y%m%d')
    # Buscar archivos que comiencen con "base_Unique_"
    archivos = [archivo for archivo in os.listdir(directorio) if archivo.startswith(buscar)]

    # Renombrar los archivos con el formato "base_Unique_yyyy_mm_dd"
    for archivo in archivos:
        viejo_nombre = os.path.join(directorio, archivo)
        nuevo_nombre = os.path.join(directorio, buscar + fecha_actual + '.xlsx')
        os.rename(viejo_nombre, nuevo_nombre)
        print(f"Archivo {viejo_nombre} renombrado como {nuevo_nombre}")

renombrar_archivo()


