import datetime
import os
import pysftp

usuario='AvalPeru'
ip='64.76.207.60'
contra='AvalPeru.01'
puerto=22
# Crear carpeta nueva
fecha_actual = datetime.datetime.now().strftime("%d_%m")
carpeta_nueva = os.path.join("D:", fecha_actual + "_UNIQUE")
os.mkdir(carpeta_nueva)

# Conectar a servidor SFTP
srv = pysftp.Connection(ip, username=usuario, password=contra, port=puerto, cnopts=pysftp.CnOpts(knownhosts='known_hosts'))

# Obtener los dos últimos archivos de /AVAL_PAGOS/
srv.cwd('/AVAL_PAGOS/')
archivos_pagos = srv.listdir()
archivos_pagos.sort(key=lambda x: srv.stat(x).st_mtime)
ultimos_pagos = archivos_pagos[-2:]

# Copiar archivos de /AVAL_PAGOS/ a carpeta_nueva/PAGOS
carpeta_pagos = os.path.join(carpeta_nueva, "PAGOS")
os.mkdir(carpeta_pagos)
for archivo in ultimos_pagos:
    srv.get(archivo, os.path.join(carpeta_pagos, archivo))

# Obtener los dos últimos archivos de /AVAL_DEUDAS/
srv.cwd('/AVAL_DEUDAS/')
archivos_deudas = srv.listdir()
archivos_deudas.sort(key=lambda x: srv.stat(x).st_mtime)
ultimos_deudas = archivos_deudas[-2:]

# Copiar archivos de /AVAL_DEUDAS/ a carpeta_nueva/DEUDAS
carpeta_deudas = os.path.join(carpeta_nueva, "DEUDAS")
os.mkdir(carpeta_deudas)
for archivo in ultimos_deudas:
    srv.get(archivo, os.path.join(carpeta_deudas, archivo))

# Cerrar conexión
srv.close()



