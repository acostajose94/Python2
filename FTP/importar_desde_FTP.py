import ftplib
import os
import time
from dateutil import parser
import datetime



fecha_hoy     = datetime.date.today()
fecha_ayer    = fecha_hoy - datetime.timedelta(1)
fecha_hoy_formato = fecha_hoy.strftime('%Y%m%d') 
fecha_ayer_formato = fecha_ayer.strftime('%Y%m%d') 
text__fecha = fecha_ayer.strftime('%d/%m/%Y') 
fomato_pago=fecha_ayer_formato+fecha_ayer_formato+'_'+fecha_hoy_formato+'.txt'
pago_ped36='PEDP36'+fomato_pago
pago_ped35='PEDP35'+fomato_pago
base_ped36='PEDP362020110199990101_'+fecha_hoy_formato
base_ped35='PEDP352020110199990101_'+fecha_hoy_formato
servidor = '64.76.207.60'
us = 'AvalPeru'
pas= 'AvalPeru.01'

print(pago_ped35)
print(pago_ped36)
print(base_ped35)
print(base_ped36)


import pysftp

myHostname = "64.76.207.60"
myUsername = "AvalPeru"
myPassword = "AvalPeru.01"
puerto='22'
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword,port=puerto) as sftp:
    





ftp = ftplib.FTP('64.76.207.60', 'AvalPeru','AvalPeru.01')
ftp.retrlines('LIST')

ftp.cwd("pub")
ftp.cwd("example")
ftp.retrlines('LIST')

names = ftp.nlst()
final_names= [line for line in names if 'client' in line]

latest_time = None
latest_name = None

for name in final_names:
        time = ftp.sendcmd("MDTM " + name)
        if (latest_time is None) or (time > latest_time):
            latest_name = name
            latest_time = time

print(latest_name)
file = open(latest_name, 'wb')
ftp.retrbinary('RETR '+ latest_name, file.write)