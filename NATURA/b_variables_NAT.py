from datetime import datetime
# Obtener la fecha actual en formato dd_mm
hoy=datetime.now()
fecha_actual =hoy.strftime('%d.%m.%y')
hoy_carpeta=hoy.strftime('%d_%m')
 
eliminar_cabecera_aveces=['Control de Envío la Pérdida',
'Fecha de Envío la Pérdida']
columnas_a_eliminar_casi_siempre = ['COLOR']

cabecera = [
    'Orden del Pedidos','Código Persona','Cod Grupo','Nombre de la Persona','Título',
'No Pedido','No Factura','Fecha Pedido','Fecha Vcto','Fecha Saldo','Original',
'Saldo','Saldo Corregido','Interés/multa Acumulados (100% descuento)',
'% Descuento Saldo Original',
'Monto Descuento Saldo Original',
'Total descuentos',
'Monto mínimo a pagar Campaña',
'Fecha Saldo Corregido',
'Días de retraso',
'Ciclo',
'Fecha nasc',
'Estructura Comercial',
'Nombre de la Estructura Comercial',
'Estructura Comercial Padre',
'Nombre de la Estructura Comercial Padre',
'DNI',
'Dirección',
'Teléfono Persona',
'Numero Celular',
'Correo Electrónico',
'TRAMO ',
'AGENCIA',
'RIESGO'
]
cabecera_nueva = [
    'ORDEN_PEDIDO',
'CODIGO_PERSONA',
'COD_GRUPO',
'NOMBRE_PERSONA',
'TITULO',
'NO_PEDIDO',
'NO_FACTURA',
'FECHA_PEDIDO',
'FECHA_VCTO',
'FECHA_SALD',
'ORIGINAL',
'SALDO',
'SALDO_CORREGIDO',
'INTERES_MULTA_ACUMULADOS_100_PORCENT',
'PORCENT_DESCUENTO_SALDO_ORIG',
'MONTO_DESCUENTO_SALDO_ORIG',
'TOTAL_DESCUENTO',
'MONTO_MIN_A_PAGAR_CAMP',
'PORCENT_DESCUENTO_SALDO_ORIG_MAX',
'MONTO_MIN_A_PAGAR_CAMP_MAX',
'FECHA_SALDO_CORREGIDO',
'DIAS_DE_RETRASO',
'CICLO',
'FECHA_NASC',
'ESTRUCTURA_COMERCIAL',
'NOMBRE_ESTRUCTURA_COMERCIAL',
'ESTRUCTURA_COMERCIAL_PADRE',
'NOMBRE_ESTRUCTURA_COMERCIAL_PADRE',
'DNI',
'DIRECCION',
'TELEFONO_PERSONA',
'NUMERO_CELULAR',
'CORREO_ELECTRONICO',
'TRAMO',
'AGENCIA',
'RIESGO'

]
 
