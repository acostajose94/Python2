from variables import *
from funciones import *
import shutil
import datetime
# conectar_VPN(img__forti,img__conectar,ip_address)

verificar_carpeta(mes_exist)

if not os.path.exists(dia_exist):
    shutil.copytree(ruta_origen,dia_exist)
    descargar_archivos_desde_servidor(dia_exist)
    renombrar_archivo(dia_exist,'base_Unique_',hoy)
    renombrar_archivo(dia_exist,'pagos_unique_',hoy)
else:
    print("La carpeta tiene archivos")




shutil.copytree(ruta_origen,dia_exist_ayer)
descargar_archivos_desde_servidor(dia_exist_ayer,1)
renombrar_archivo(dia_exist_ayer,'base_Unique_',ayer)
renombrar_archivo(dia_exist_ayer,'pagos_unique_',ayer)

shutil.copytree(ruta_origen,dia_exist_ante_ayer)
descargar_archivos_desde_servidor(dia_exist_ante_ayer,2)
renombrar_archivo(dia_exist_ante_ayer,'base_Unique_',ante_ayer)
renombrar_archivo(dia_exist_ante_ayer,'pagos_unique_',ante_ayer)

