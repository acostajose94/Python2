import datetime
import os

code_ubica=os.getcwd()
folder__destino = r'C:\Users\avalp\Downloads\yyyy-mm-dd\\'
zip_ubicacion   = r'C:\Users\avalp\Downloads\reportes_historicos_3.zip'
img__forti      = r'C:\Users\avalp\OneDrive\Escritorio\python\ejecutar\img\forti.png'
img__conectar   = r'C:\Users\avalp\OneDrive\Escritorio\python\ejecutar\img\conectar.png'
img__excel      = r'C:\Users\avalp\OneDrive\Escritorio\python\logo__excel.png'
img__visual     =r'C:\Users\avalp\OneDrive\Escritorio\python\visual.png'
img__refesh     = r'C:\Users\avalp\OneDrive\Escritorio\python\refresh.png'
img__pop_up     = r'C:\Users\avalp\OneDrive\Escritorio\python\pop_up.png'
img__listo      = r'C:\Users\avalp\OneDrive\Escritorio\python\listo.png'
img__listo_ejecutando  = r'C:\Users\avalp\OneDrive\Escritorio\python\listo_ejecutando.png'
img__next       = r'C:\Users\avalp\OneDrive\Escritorio\python\img__next.png'
img__prev       = r'C:\Users\avalp\OneDrive\Escritorio\python\img__prev2.png'
img__base10     = r'C:\Users\avalp\OneDrive\Escritorio\python\base10.png'
img__bm         = r'C:\Users\avalp\OneDrive\Escritorio\python\img__bm.png'
img__formato    = r'C:\Users\avalp\OneDrive\Escritorio\python\img__formato.png'
img__bn         = r'C:\Users\avalp\OneDrive\Escritorio\python\img__bn.png'
folder__mover   = r'C:\Users\avalp\OneDrive\Escritorio\\'
text            = 'avalperu2020*$'
confidence =0.9
confidence2 =0.8
count = 0
n_clicks = 10
#fecha_hoy     = datetime.date.today()
fecha_ayer    = datetime.date.today() - datetime.timedelta(1)
fecha_formato = fecha_ayer.strftime('%Y%m%d') 
text__fecha = fecha_ayer.strftime('%d/%m/%Y')
fecha_carpeta= fecha_ayer.strftime('%Y-%m-%d')