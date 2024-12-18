
from openpyxl import load_workbook
from pagos_variables import *
from pagos_funciones import *


# eliminar_archivos_excel(ruta_actual)
archivo_reciente=extraer_archivo_mas_reciente(ruta_actual)

# Buscar archivo más reciente con 'TLS'
# archivo_tls = buscar_archivo_mas_reciente(ruta_actual, palabra_tls)
# Buscar archivo más reciente con 'certus'

# Buscar archivo más reciente con 'campus'
archivo_campus = buscar_archivo_mas_reciente(ruta_actual, 'CAMPUS')
if archivo_campus != None:
# #Pagos de CERTUS
    # pagos_campus
    pagos_campus(archivo_campus,cabecera_esperada,nueva_cabecera,fecha_actual)

archivo_certus = buscar_archivo_mas_reciente(ruta_actual, palabra_certus)
if archivo_certus != None:
# #Pagos de CERTUS
    pagos_certus(archivo_certus,cabecera_esperada,nueva_cabecera,fecha_actual)



#Pagos de TLS
# pagos_tls(archivo_tls,fecha_actual)

# os.remove(archivo_reciente)

