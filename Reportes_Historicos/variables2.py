import datetime
import os

code_ubica=os.getcwd()
carp_imagen=code_ubica+'\imagenes'

folder__destino = r'C:\Users\avalp\Downloads\yyyy-mm-dd2\\'
zip_ubicacion   = r'C:\Users\avalp\Downloads\yyyy-mm-dd2.zip'
img__forti      = r''+carp_imagen+'\\forti.png'
img__conectar   = r''+carp_imagen+'\\conectar.png'
img__excel      = r''+carp_imagen+'\\logo__excel.png'
img__visual     = r''+carp_imagen+'\\visual.png'
img__py_eje     = r''+carp_imagen+'\\py_eje.png'
img__refesh     = r''+carp_imagen+'\\refresh.png'
img__pop_up     = r''+carp_imagen+'\\pop_up.png'
img__listo      = r''+carp_imagen+'\\listo.png'
img__listo_ejecutando  = r''+carp_imagen+'\listo_ejecutando.png'
img__next       = r''+carp_imagen+'\\img__next.png'
img__prev       = r''+carp_imagen+'\\img__prev2.png'
img__base10     = r''+carp_imagen+'\\base10.png'
img__bm         = r''+carp_imagen+'\\img__bm.png'
img__formato    = r''+carp_imagen+'\\img__formato.png'
img__bn         = r''+carp_imagen+'\\img__bn.png'
folder__mover   = r'C:\Users\avalp\OneDrive\Escritorio\\'
text            = 'avalperu2020*$'
ip_address = '192.168.10.45'
confidence =0.9
confidence2 =0.8
count = 0
n_clicks = 10

fecha_ayer    = datetime.date.today() - datetime.timedelta(1)
fecha_formato = fecha_ayer.strftime('%Y%m%d') 
text__fecha = fecha_ayer.strftime('%d/%m/%Y')
fecha_carpeta= fecha_ayer.strftime('%Y-%m-%d')

fecha_actual      = datetime.datetime.now()
dia_semana = fecha_actual.weekday()
hora_actual = fecha_actual.hour



# Ruta de la carpeta local que deseas subir
carpeta_local = r'C:\Users\avalp\OneDrive\Escritorio\2023-05-16\\'

# ID de la carpeta compartida de Google Drive
carpeta_drive_id = '19U0E1FrynnQgp77XS2LtJryzDABwCx9I'
