from variables import *
from funciones import *
import shutil

# conectar_VPN(img__forti,img__conectar,ip_address)

verificar_carpeta(mes_exist)
if not os.path.exists(dia_exist):
    shutil.copytree(ruta_origen,dia_exist)
else:
    print("La carpeta tiene archivos")
    
    
descargar_archivos_desde_servidor(dia_exist)
