import os
import datetime
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
# from variables import *
folder__destino = r'C:\Users\Lenovo\Downloads\yyyy-mm-dd\\'
zip_ubicacion   = r'C:\Users\Lenovo\Downloads\reportes_historicos_2.zip'
img__excel      = r'C:\Users\Lenovo\Desktop\python\logo__excel.png'
img__visual     =r'C:\Users\Lenovo\Desktop\python\visual.png'
img__refesh     = r'C:\Users\Lenovo\Desktop\python\refresh.png'
img__pop_up     = r'C:\Users\Lenovo\Desktop\python\pop_up.png'
img__listo      = r'C:\Users\Lenovo\Desktop\python\listo.png'
img__listo_ejecutando  = r'C:\Users\Lenovo\Desktop\python\listo_ejecutando.png'
img__next       = r'C:\Users\Lenovo\Desktop\python\img__next.png'
img__prev       = r'C:\Users\Lenovo\Desktop\python\img__prev2.png'
img__base10     = r'C:\Users\Lenovo\Desktop\python\base10.png'
nom_avon        = 'Avon'
text            = 'avalperu2020*$'
confidence =0.9
confidence2 =0.8
count = 0
n_clicks = 7
fecha_hoy     = datetime.date.today()
fecha_ayer    = fecha_hoy - datetime.timedelta(1)
fecha_formato = fecha_ayer.strftime('%Y%m%d') 
text__fecha = fecha_ayer.strftime('%d/%m/%Y') 