import time
import pyautogui
import ctypes
import os
import zipfile

format__btn=r'C:\Users\avalp\Desktop\python\format__btn.png'

def buscarImagen_high(imagen):
    time.sleep(5)
    variable = pyautogui.locateCenterOnScreen(imagen, grayscale=True, confidence = 1)
    while variable == None:
        time.sleep(5)
        variable = pyautogui.locateCenterOnScreen(imagen, grayscale=True, confidence = 1)
        print('no variable')
    return variable

def buscarImagen(imagen):
    time.sleep(5)
    variable = pyautogui.locateCenterOnScreen(imagen, grayscale=True, confidence = 0.8)
    while variable == None:
        time.sleep(5)
        variable = pyautogui.locateCenterOnScreen(imagen, grayscale=True, confidence = 0.7)
        print('no variable')
    return variable

def buscarImagen__low(imagen):
    time.sleep(3)
    variable = pyautogui.locateCenterOnScreen(imagen, grayscale=True, confidence = 0.6)
    while variable == None:
        time.sleep(5)
        variable = pyautogui.locateCenterOnScreen(imagen, grayscale=True, confidence = 0.5)
        print('no variable')
    return variable

def crear_carpeta_si_no_existe(ruta):
    os.makedirs(ruta, exist_ok=True)
    if not os.path.exists(ruta):
        print("Error al crear la carpeta:", ruta)
        return False
    return True


def descomprimir_archivo(zip_ubicacion, folder_destino):
    with zipfile.ZipFile(zip_ubicacion, "r") as zip_ref:
        zip_ref.extractall(folder_destino)
    print("Archivos descomprimidos")


def renombrar_archivos(folder_destino, fecha_formato):
    count = 0
    for archivo in os.scandir(folder_destino):
        if archivo.is_file():
            source_name = archivo.path
            f_name = archivo.name.rsplit(" ", 1)[0]
            new_name = os.path.join(folder_destino, f"{f_name} {fecha_formato}.xlsx")
            os.rename(source_name, new_name)
            count += 1
    print(f"Archivos renombrados: {count}")

def formato__fecha():
    pyautogui.press('enter', presses=2, interval=0.25) 
    pyautogui.press('down', presses=3, interval=0.25)
    pyautogui.press('enter')           
    
def is_capslock_on():
    return ctypes.windll.user32.GetKeyState(0x14) != 0


