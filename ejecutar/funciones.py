import time
import pyautogui
import ctypes
import os
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

def verifica_carp(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print("Carpeta creada")
    else:
        print("Ya esta")



