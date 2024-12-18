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


# visual=buscarImagen__low(img__visual)
# pyautogui.click(visual)   

forti=buscarImagen(img__forti)
pyautogui.click(forti)
time.sleep(12)

conecta=buscarImagen(img__conectar)
pyautogui.click(conecta)
time.sleep(58)


# crea folder si no existe
isExist = os.path.exists(folder__destino)
if not isExist:
  os.makedirs(folder__destino)
  print("The new directory is created!")

listar = os.listdir(folder__destino)
numero_archivos = len(listar)
print(numero_archivos)

if numero_archivos < 1:
    print('no hay archivos en la carpeta')
    print(numero_archivos)


    #Descomprime
    with zipfile.ZipFile(zip_ubicacion,"r") as zip_ref:
        zip_ref.extractall(folder__destino)
    zip_ref.close() 
    print('Archivos Descomprimidos')

    for file_name in os.listdir(folder__destino):
            # #Construct old file name
            source_name = folder__destino + file_name
            f_name=file_name.rsplit(' ', 1)[0]
            new_name = folder__destino + f_name + " " + fecha_formato + ".xlsx"

            # Renaming the file
            os.rename(source_name, new_name)

            count += 1
    print('Archivos Renombrados')
    print(count)
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

            # wb.Save()
            # print('Guardado')
            #click a la derecha
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
            final_str=folder__destino[:-1]
            td = final_str+nombre+' (TD).xlsx'
            time.sleep(5)
            print(td)
            
            wb.SaveAs(td)
            print('TD guardado')
            #salir y esperar
            xlapp.Quit()
            visual=buscarImagen(img__visual)
            pyautogui.click(visual)   

            os.remove(archivo_destino) 
            # shutil.move(archivo_destino, folder__mover)
            isExist = os.path.exists(folder__mover+fecha_carpeta)
            if not isExist:
                os.makedirs(folder__mover+fecha_carpeta)
                print("The new directory is created!")
            shutil.move(td,folder__mover+fecha_carpeta)
            print('finished')
    
