import datetime
import locale
import os
# Configurar el idioma local en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Direcciones
carpeta_b=r"\\192.168.100.45\\Clientes\\62. Unique\\2024\\"
ruta_origen = r"V:\62. Unique\2023\dd-mm\\" 

hoy=datetime.datetime.now()
ayer=hoy- datetime.timedelta(days=1)
ante_ayer=ayer- datetime.timedelta(days=1)
# mes_anterior=hoy.replace(month=hoy.month-1)

# Obtener el mes actual
num_dia = hoy.strftime('%d')
num_dia_ayer = ayer.strftime('%d')
num_dia_ante_ayer = ante_ayer.strftime('%d')

num_mes = hoy.strftime('%m')
name_mes = hoy.strftime('%B')[:3].capitalize()
c_mes=num_mes+'_'+name_mes+'_'+'Unique'

# Existe mes y y dia
mes_exist=carpeta_b+c_mes

dia_exist=mes_exist+'\\'+num_dia+'_'+num_mes
dia_exist_ayer=mes_exist+'\\'+num_dia_ayer+'_'+num_mes
dia_exist_ante_ayer=mes_exist+'\\'+num_dia_ante_ayer+'_'+num_mes

# Ubicacion codigo e imagenes
code_ubica=os.getcwd()
carp_imagen=code_ubica+'\imagenes'
img__forti      = r''+carp_imagen+'\\forti.png'
img__conectar   = r''+carp_imagen+'\\conectar.png'


# Conexion VPN
ip_address = '172.23.23.119'
usuario='AvalPeru'
ip='64.76.207.60'
contra='AvalPeru.01'
puerto=22