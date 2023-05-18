import os
import time
import pyautogui
import subprocess
import pysftp
import datetime
from variables import usuario,ip,contra,puerto

def verificar_carpeta(ruta_carpeta):
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"Carpeta creada")
    else:
        print(f"Carpeta existe")


def buscarImagen(imagen):
    time.sleep(5)
    variable = pyautogui.locateCenterOnScreen(imagen, grayscale=True, confidence = 0.8)
    while variable == None:
        time.sleep(5)
        variable = pyautogui.locateCenterOnScreen(imagen, grayscale=True, confidence = 0.7)
        print('no variable')
    return variable

def conectar_VPN(img__forti,img__conectar,ip_address):
    ping_output = subprocess.run(["ping", "-n", "1", ip_address], capture_output=True)

    if ping_output.returncode != 0:
        forti=buscarImagen(img__forti)
        pyautogui.click(forti)
        time.sleep(12)

        conecta=buscarImagen(img__conectar)
        pyautogui.click(conecta)
        time.sleep(58)



def descargar_archivos_desde_servidor(carpeta_destino,day=0,ip=ip, usuario=usuario, contra=contra, puerto=puerto):
    # Crear carpeta de destino con fecha actual
    fecha_actual = datetime.datetime.now().strftime("%d_%m")
    carpeta_nueva = carpeta_destino
    # Conectar a servidor SFTP
    srv = pysftp.Connection(ip, username=usuario, password=contra, port=puerto, cnopts=pysftp.CnOpts(knownhosts='known_hosts'))

    try:
        # Obtener los dos últimos archivos de /AVAL_PAGOS/
        srv.cwd('/AVAL_PAGOS/')
        archivos_pagos = srv.listdir()
        archivos_pagos.sort(key=lambda x: srv.stat(x).st_mtime)
        
        
        if day==0:
            ultimos_pagos = archivos_pagos[-2:]
        else:
            ultimos_pagos = archivos_pagos[-4:-2]

        # Copiar archivos de /AVAL_PAGOS/ a carpeta_nueva/PAGOS
        carpeta_pagos = os.path.join(carpeta_nueva, "AVAL_PAGOS")
        # os.mkdir(carpeta_pagos)
        for archivo in ultimos_pagos:
            srv.get(archivo, os.path.join(carpeta_pagos, archivo))

        # Obtener los dos últimos archivos de /AVAL_DEUDAS/
        srv.cwd('/AVAL_DEUDAS/')
        archivos_deudas = srv.listdir()
        archivos_deudas.sort(key=lambda x: srv.stat(x).st_mtime)
        
        if day==0:    
            ultimos_deudas = archivos_deudas[-2:]
        else:
            ultimos_deudas = archivos_deudas[-4:-2]

        # Copiar archivos de /AVAL_DEUDAS/ a carpeta_nueva/DEUDAS
        carpeta_deudas = os.path.join(carpeta_nueva, "AVAL_DEUDAS")
        # os.mkdir(carpeta_deudas)
        for archivo in ultimos_deudas:
            srv.get(archivo, os.path.join(carpeta_deudas, archivo))
    finally:
        # Cerrar conexión
        srv.close()
        
    
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




