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

def formato__fecha():
    pyautogui.press('enter', presses=2, interval=0.25) 
    pyautogui.press('down', presses=3, interval=0.25)
    pyautogui.press('enter')           
    
def is_capslock_on():
    return ctypes.windll.user32.GetKeyState(0x14) != 0


def crear_carpeta_si_no_existe(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print("The new directory is created!")
    else:
        print("Ya esta")

def descomprimir_archivo(zip_ubicacion, folder_destino):
    with zipfile.ZipFile(zip_ubicacion, "r") as zip_ref:
        zip_ref.extractall(folder_destino)
    print("Archivos descomprimidos")
    
    
def conectar_VPN(img__forti,img__conectar):
    forti=buscarImagen(img__forti)
    pyautogui.click(forti)
    time.sleep(12)

    conecta=buscarImagen(img__conectar)
    pyautogui.click(conecta)
    time.sleep(58)
        
def renombrar_archivos(folder_destino, fecha_formato):
    for file_name in os.listdir(folder_destino):
        # Construye el nombre del archivo antiguo y el nuevo nombre
        source_name = os.path.join(folder_destino, file_name)
        f_name = file_name.rsplit(' ', 1)[0]
        new_name = os.path.join(folder_destino, f_name + " " + fecha_formato + ".xlsx")

        # Renombra el archivo
        os.rename(source_name, new_name)

    print('Archivos Renombrados')
    
