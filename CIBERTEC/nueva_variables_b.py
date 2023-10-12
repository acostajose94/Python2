import datetime

arch1='Base Asignacion Inactiva I Julio.xlsx'
arch2='Base Asignacion Inactiva II Julio.xlsx'
arch3='Base Asignacion Inactiva III Julio.xlsx'
arch4='Base Asignacion Inactiva IV Julio.xlsx'
arch5='Base Asignacion Inactiva V Julio.xlsx'
arch6='Base Inactiva Formacion continua Julio.xlsx'

arch7='Base Asignacion  Inactiva Diplomado - wetalk Julio.xlsx'
dfs_modificados = []
# Nombres de los archivos de Excel
archivos_excel = [arch7,arch1,arch2,arch3,arch4,arch5,arch6,arch7]

arch8='Base Asignacion Activa 2023-1 Julio 18 - 31 Final.xlsx'
dfs_modificados2 = []
archivos_excel2 = [arch8]

fecha_actual = datetime.datetime.now().strftime('%d_%m')