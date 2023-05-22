from variables import *
from funciones import *
import shutil

# conectar_VPN(img__forti,img__conectar,ip_address)

if not os.path.exists(dia_exist):
    shutil.copytree(ruta_origen,dia_exist)
    descargar_archivos_desde_servidor(dia_exist)
    renombrar_archivo(dia_exist,'base_Unique_',hoy)
    renombrar_archivo(dia_exist,'pagos_unique_',hoy)
else:
    print("La carpeta tiene archivos")



if datetime.datetime.today().weekday() == 0:
    if not os.path.exists(dia_exist_ayer):
        shutil.copytree(ruta_origen,dia_exist_ayer)
        descargar_archivos_desde_servidor(dia_exist_ayer,1)
        renombrar_archivo(dia_exist_ayer,'base_Unique_',ayer)
        renombrar_archivo(dia_exist_ayer,'pagos_unique_',ayer)
else:
    print("Hoy no es lunes")
