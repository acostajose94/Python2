import os
import zipfile
import win32com.client
from openpyxl import Workbook
import time     
import keyboard
import pyautogui
import win32api
import win32con
import pyperclip
 
 
from funciones import *
from variables2 import *
import datetime
import shutil
import threading
import tkinter as tk
import pythoncom
import sys
import subprocess

def stop():
        try:
            root.destroy()
            sys.exit(1)
        except SystemExit:
            pass

if dia_semana < 5:

    def play():
        
        ping_output = subprocess.run(["ping", "-n", "1", ip_address], capture_output=True)

        if ping_output.returncode != 0:
            conectar_VPN(img__forti,img__conectar)
        
        # crea dd-mm-yyyy
        crear_carpeta_si_no_existe(folder__destino)
        # Crea carpeta del dia
        crear_carpeta_si_no_existe(folder__mover+fecha_carpeta)
        
        listar = os.listdir(folder__destino)
        numero_archivos = len(listar)
        print(numero_archivos)

        if numero_archivos < 1:
            print('no hay archivos en la carpeta')
            descomprimir_archivo(zip_ubicacion,folder__destino)
            renombrar_archivos(folder__destino, fecha_formato)
        pythoncom.CoInitialize()
        for file_name in os.listdir(folder__destino):
                
                xlapp = win32com.client.DispatchEx("Excel.Application")
                # Open the workbook in said instance of Excel
                archivo_destino=folder__destino + file_name
                print(archivo_destino)
                wb = xlapp.Workbooks.Open(archivo_destino)
                xlapp.DisplayAlerts = True
                xlapp.Visible = True
                xlMaximized = -4137
                # Para pantalla completa
                xlapp.WindowState = xlMaximized
                print('Archivo Obtenido')
                
                #click excel
                logo=buscarImagen(img__excel)
                pyautogui.click(logo) 
            
                
                #Escribir Fecha Interna
                print(text__fecha)
                pyautogui.write(text__fecha)
                pyautogui.press('enter') 

                #refresh Click
                refresh=buscarImagen(img__refesh)

                pyautogui.click(refresh)
                time.sleep(8)
                print('Escribiendo Clave')
                pyautogui.write(text)
                time.sleep(8)
                pyautogui.press('enter') 

                xlapp.CalculateUntilAsyncQueriesDone() 
                print('Primer refresh')  
                

                wb.RefreshAll()
                xlapp.CalculateUntilAsyncQueriesDone()
                print('Segundo refresh')
    
                if 'Avon' in file_name:
                    time.sleep(18)
                    print(file_name)
                    next__btn=buscarImagen(img__next)
                    pyautogui.click(next__btn,clicks = n_clicks, interval=0.5) 

                    #Boton base
                    base__btn=buscarImagen(img__base10)
                    pyautogui.click(base__btn) 
                    time.sleep(8)
                    #Formato Fecha
                    columna__btm=buscarImagen(img__bm)
                    pyautogui.click(columna__btm)
                    format__btn=buscarImagen(img__formato)
                    pyautogui.click(format__btn)
                    formato__fecha()
                    pyautogui.click(columna__btm)
                    time.sleep(8)
                    #Formato Fecha
                    columna__btn=buscarImagen(img__bn)
                    pyautogui.click(columna__btn)
                    pyautogui.click(format__btn)
                    formato__fecha()
                    pyautogui.click(columna__btn)
                    time.sleep(8)
                    #Ir al inicio
                    prev__btn =buscarImagen(img__prev)
                    pyautogui.click(prev__btn)  
                    time.sleep(8)   

                    wb.RefreshAll()
                    xlapp.CalculateUntilAsyncQueriesDone()
                    print('tercer refresh')

                 
                next__btn=buscarImagen(img__next)
                pyautogui.click(next__btn,clicks = n_clicks, interval=0.5) 

                #click derecho, abajo y enter
                base__btn=buscarImagen(img__base10)
                pyautogui.rightClick(base__btn) 
                pyautogui.press('down', presses=2)
                pyautogui.press('enter', presses=2) 
                time.sleep(30)
                #click a la izquierda
                prev__btn =buscarImagen(img__prev)
                pyautogui.click(prev__btn) 
                
                nombre=file_name.rsplit('.', 1)[0]
                final_str=folder__mover[:-1]+fecha_carpeta
                td = final_str+'\\'+nombre+' (TD).xlsx'
                time.sleep(5)
                print(td)
                
                wb.SaveAs(td)
                print('TD guardado')
                #salir y esperar
                xlapp.Quit()
                visual=buscarImagen(img__visual)
                pyautogui.click(visual)   

                os.remove(archivo_destino) 
                print('finished')
    
                if is_paused:
                    break

    def start_play_thread():
        global play_thread, is_paused
        is_paused = False
        play_thread = threading.Thread(target=play)
        play_thread.start()

    def pausa():
        global is_paused
        is_paused = True

    
    root = tk.Tk()
    
    root.title('Reportes Hist')

    def keep_on_top():
        root.attributes('-topmost', True)
        root.after(100, keep_on_top)

    is_paused = False
    play_thread = None

    play_button = tk.Button(root, text="Play", command=start_play_thread)
    pause_button = tk.Button(root, text="Pausa", command=pausa)
    stop_button = tk.Button(root, text="Stop", command=stop)

    play_button.pack()
    pause_button.pack()
    stop_button.pack()


    # Obtenemos la altura de la pantalla y la dividimos por 2 para obtener la mitad de la altura
    screen_height = root.winfo_screenheight()
    half_screen_height = int(screen_height / 2)

    # Establecemos la altura de la ventana
    window_height = 100

    # Establecemos la anchura de la ventana
    window_width = 200

    # Establecemos la posición x de la ventana para que aparezca en la derecha de la pantalla
    x_position = int(root.winfo_screenwidth() - window_width)

    # Establecemos la posición y de la ventana para que aparezca centrada verticalmente
    y_position = half_screen_height - int(window_height / 2)

    # Establecemos la posición y la anchura y altura de la ventana
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_position, y_position))

    if hora_actual < 7:
        start_play_thread()


    keep_on_top()
    root.mainloop()

else:
    # Si es sábado o domingo entre las 5 y las 6 de la mañana
    if dia_semana == 5 or dia_semana == 6:
        if  hora_actual < 6:
            # Apagar la PC
            os.system("shutdown /s /t 10")
            print("Apagando la PC...")
        else:
            print("Hoy no es un día hábil ni la hora para apagar la PC")
            stop()
    else:
        print("Hoy no es un día hábil ni la hora para apagar la PC")
        stop()