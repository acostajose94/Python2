import os

# Definir cabecera esperada
cabecera_esperada = ['UNE', 'COD_ALUMNO', 'PIDM', 'NOMBRES', 'APELLIDOS', 'NIVEL','NIVEL_DESCRIPCION','NUM_COMPROBANTE',
                     'NUM_COMPROBANTE', 'FEC_VENCIMIENTO', 'TRAN_CARGO', 'COD_CARGO', 'DESC_CARGO', 'IMP_CARGO', 'IMP_DSCTO',
                  'IMP_NETO', 'IMP_NC', 'IMP_PAGO', 'IMP_SALDO', 'FEC_HOR_PAG_TRAN', 'FEC_HOR_PAG_REG', 'FEC_PAG_TRAN',
                  'FEC_PAG_REG', 'COD_MEDIO_PAGO', 'DESC_MEDIO_PAGO', 'TRAN_PAGO', 'PERIODO', 'PROGRAMA',
                  'DESC_PROGRAMA', 'SEDE', 'TIPO_ALUMNO', 'ESTADO_ALUMNO', 'CICLO_ALUMNO', 'DIAS_PAGO_TRAN',
                  'DIAS_ATRASO_TRAN', 'DIAS_PAGO_REG', 'DIAS_ATRASO_REG']

nueva_cabecera =    ['UNE', 'COD_ALUMNO', 'PIDM', 'NOMBRES', 'APELLIDOS', 'NUM_COMPROBANTE', 'FEC_VENCIMIENTO', 'TRAN_CARGO',
                  'COD_CARGO', 'DESC_CARGO', 'IMP_CARGO', 'IMP_DSCTO', 'IMP_NETO', 'IMP_NC', 'IMP_PAGO', 'IMP_SALDO',
                  'FEC_HOR_PAG_TRAN', 'FEC_HOR_PAG_REG', 'FEC_PAG_TRAN', 'FEC_PAG_REG', 'COD_MEDIO_PAGO',
                  'DESC_MEDIO_PAGO', 'TRAN_PAGO', 'PERIODO', 'PROGRAMA', 'DESC_PROGRAMA', 'SEDE', 'TIPO_ALUMNO',
                  'ESTADO_ALUMNO', 'CICLO_ALUMNO', 'DIAS_PAGO_TRAN', 'DIAS_ATRASO_TRAN', 'DIAS_PAGO_REG',
                  'DIAS_ATRASO_REG']
# Directorio donde se encuentran los archivos
directorio = ''
ruta_actual = os.path.dirname(os.path.abspath(__file__))
# Palabra a buscar
palabra_tls = 'TLS'
palabra_certus = 'CERTUS'

from datetime import datetime
# Obtener la fecha actual en formato dd_mm
hoy=datetime.now()
fecha_actual =hoy.strftime('%d_%m')


cab_campus_orden=['UN',
'ID',
'NO_HAY_DATA',
'Nombres',
'Apellidos',
'Nº Factura',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'Importe Pagado',
'NO_HAY_DATA',
'Importe Pagado',
'NO_HAY_DATA',
'Importe Pagado',
'NO_HAY_DATA',
'Fecha Pago',
'Fecha Pago',
'Fecha Pago',
'Fecha Pago',
'NO_HAY_DATA',
'Descripción',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA'
]