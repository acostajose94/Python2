from datetime import datetime
# Obtener la fecha actual en formato dd_mm
hoy=datetime.now()
fecha_actual =hoy.strftime('%d.%m')
hoy_carpeta=hoy.strftime('%d_%m')
fecha_dmy=hoy.strftime("%d/%m/%Y")
 


cab_esperada=[
'SEGMENTO',
'FECHAPROCESO',
'CUENTA_BT',
'CODIGO_ICS',
'OPERACION',
'TIPO_OP',
'MODULO',
'SUCURSAL',
'FECHA_SURT',
'FECFIN_CRONOG',
'TASA',
'TASA_MORA',
'TASA_ACTUAL',
'TASA_MORA_ACTUAL',
'DIASMORA',
'DIA_ATRASO',
'DIA_PAGO',
'IMPORTE_ORIGINAL',
'CUOTA',
'CAPITAL',
'RANGOCAPITAL',
'CAPITAL_AMORTIZADO',
'CAPITAL_MORA',
'DEUDA_ACTUAL',
'REQUERIDO',
'SALDOTOTAL',
'INT_ADEUDADOS',
'INT_COMPENSATORIO',
'INT_DEVENGADOS',
'INT_MORA',
'INT_PUNITORIO',
'FEC_ULTCUOTA_VENC',
'FECHAPROXPAGO',
'FEC_CANCELACION',
'FEC_ULT_PAGO',
'NUM_CUOTA_TOTAL',
'NUM_CUOTA_PAGADO',
'NUM_CUOTA_PEND',
'NUM_CUOTA_SINPAGO',
'ESCASTIGO',
'FEC_CASTIGO',
'RANGOCASTIGO',
'DNI',
'Nombres',
'AP_PATERNO',
'AP_MATERNO',
'FEC_NAC',
'Sexo',
'SituacionLaboral',
'EstadoCivil',
'GradoInstrucion',
'Ubigeo',
'DIRECCION',
'Departamento',
'Provincia',
'Distrito',
'TELF_1',
'TELF_2',
'TELF_3',
'TELF_4',
'TELF_5',
'CLASIFICACION_BAZ',
'POLIGONO',
'CITY',
'GERENCIA',
'REGION',
'ZONA',
'ESTATUS_CLIENTE',
'PRIORIDAD',
'RIESGO',
'REFINANCIADO',
'EMPRESA',
'CAMPANA',
'DSCTO',
'MONTO_CAMPANA',
'RESPONSABLE',
'VENTA_CARTERA',
'TELF_GEST_N-1',
'TELF_GEST_N-2',
'TELF_GEST_N-3',
'TELF_GEST_N-4',
'TELF_GEST_N-5',
'DSCTO_REAL'

]

cab_ordenada=[
'FECHAPROCESO',
'CUENTA_BT',
'CODIGO_ICS',
'DNI',
'NO_HAY_DATA',
'DIA_ATRASO',
'NO_HAY_DATA',
'SALDOTOTAL',
'CAPITAL',
'RANGOCAPITAL',
'REQUERIDO',
'CUOTA',
'NO_HAY_DATA',
'DIA_PAGO',
'Nombres',
'AP_PATERNO',
'AP_MATERNO',
'RIESGO',
'PRIORIDAD',
'TELF_GEST_N-1',
'TELF_GEST_N-2',
'TELF_GEST_N-3',
'TELF_GEST_N-4',
'TELF_GEST_N-5',
'RESPONSABLE',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'FEC_ULT_PAGO',
'FECHA_SURT',
'FECHAPROXPAGO',
'SituacionLaboral',
'DIRECCION',
'Distrito',
'Provincia',
'Departamento',
'REGION',
'GERENCIA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'MONTO_CAMPANA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA'
 
]

cab_nueva=[
'FECHAPROCESO',
'CUENTA_BT',
'CODIGO_ICS',
'DNI',
'PERIODO_ATRASO',
'DIA_ATRASO',
'RANGO_ATRASO',
'SALDOTOTAL',
'CAPITAL',
'RANGOCAPITAL',
'REQUERIDO',
'CUOTA',
'CUOTA_MAYORATRASO',
'DIA_PAGO',
'FCCTENOMBRE',
'FCCTEAPATERNO',
'FCCTEAMATERNO',
'RIESGO',
'PRIORIDAD',
'TELF_1',
'TELF_2',
'TELF_3',
'TELF_4',
'TELF_5',
'EMPRESA',
'CLIENTE_FPD',
'CLASIF_INTERNA',
'CLASIF_EXTERNA',
'TIPO_CLIENTE',
'PAGOLINK',
'FULTIMOPAGO',
'FECHA_SURT',
'FECHAPROXPAGO',
'SITUACION_LABORAL',
'DIRECCION',
'Distrito',
'Provincia',
'Departamento',
'REGION',
'GERENCIA',
'FLAG_ORIGEN_CARTERA',
'TIPO_CONTACTO_CAMPO',
'CAMP_REFI',
'CAMP_LIQUI',
'CAMP_PKM_N',
'CAMP_PKM_C',
'APLICA_SEG_DEUDA_PROT',
'MONTO_PAGO_MES',
'STATUS_CAMPAÑA',
'CAMPANA_ORIGEN'
]

