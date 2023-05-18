from variables import *
from funciones import *
import shutil
import datetime
# conectar_VPN(img__forti,img__conectar,ip_address)

verificar_carpeta(mes_exist)

if not os.path.exists(dia_exist):
    shutil.copytree(ruta_origen,dia_exist)
    descargar_archivos_desde_servidor(dia_exist)
else:
    print("La carpeta tiene archivos")



# if datetime.datetime.today().weekday() == 0:
if not os.path.exists(dia_exist_ayer):
    shutil.copytree(ruta_origen,dia_exist_ayer)
    descargar_archivos_desde_servidor(dia_exist_ayer,1)
else:
    print("Hoy no es lunes")
