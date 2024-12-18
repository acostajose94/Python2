from datetime import datetime
# Obtener la fecha actual en formato dd_mm
hoy=datetime.now()
fecha_actual =hoy.strftime('%d.%m')
hoy_carpeta=hoy.strftime('%d_%m')
fecha_dmy=hoy.strftime("%d/%m/%Y")
 
eliminar_cabecera_aveces=['Control de Envío la Pérdida',
'Fecha de Envío la Pérdida']
columnas_a_eliminar_casi_siempre = ['COLOR']

#Cabecera Esperada
cab_esperada=['NúmeroPedido',
'CicloCaptacion',
'Grupo',
'FechaPedido',
'FechaVencimientoOriginal',
'ValorTítulo',
'Saldo actualizado',
'Estructura Padre',
'Estructura',
'CódigoPersona',
'Nombre',
'Teléfono Residencial',
'Teléfono móvil',
'Correo electrónico personal',
'Agencia',
'Status actual',
'Pago',
'Fecha de pago',
'Validacion de pago',
'Monto recuperado',
'Contador',
'Saldo actualizado VF',
'DNI',
'Color'
]
#Nuevo orden
nuevo_orden_prev = [
    'NO_HAY_DATA',
'CódigoPersona',
'Grupo',
'Nombre',
'NO_HAY_DATA',
'NúmeroPedido',
'NO_HAY_DATA',
'FechaPedido',
'FechaVencimientoOriginal',
'NO_HAY_DATA',
'Saldo actualizado',
'Saldo actualizado VF',
'Saldo actualizado VF',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'Saldo actualizado VF',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
'Estructura',
'NO_HAY_DATA',
'Estructura Padre',
'DNI',
'NO_HAY_DATA',
'Teléfono Residencial',
'Teléfono móvil',
'Correo electrónico personal',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',


]
# Lista con el orden de las columnas deseadas
orden_previo = [
    'Orden del Pedido',
    'Código Consultora',
    'Grupo Lider',
    'Nombre Consultora',
    'NO_HAY_DATA',
    'Nro Pedido',
    'NO_HAY_DATA',
    'Fecha Pedido',
    'Fecha Vcto',
    'NO_HAY_DATA',
    'Valor Original',
    'Saldo',
    'Saldo Corregido',
    'Interés/Multa Acumulados',
    '% Descuento Saldo',
    'Monto Descuento Saldo',
    'Total Descuentos',
    'Monto mínimo a pagar Campaña',
    'NO_HAY_DATA',
    'Días de Retraso',
    'Ciclo',
    'Fecha Nacimiento',
    'NO_HAY_DATA',
    'NO_HAY_DATA',
    'NO_HAY_DATA',
    'NO_HAY_DATA',
    'DNI',
    'Dirección',
    'Teléfono 1',
    'Teléfono 2',
    'Correo',
    'Tramo Vencimiento',
    'Agencia',
    'Riesgo'
]


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
 


#CABECERA_PAGOS

orden_cabecera_pagos=[
    'NúmeroPedido',
'NO_HAY_DATA',
'Fecha de pago',
'Pago',
'NO_HAY_DATA',
'CódigoPersona',
'Nombre',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA'   
]
cabecera_pagos=[
'NRO_PEDIDO',
'CodigoTitulo',
'FECHA_PAGO',
'PAGOS',
'EntidadDondeFueRealizadoElPago',
'CODIGO_PERSONA',
'Persona',
'Fecha_de_asignacion',
'Tramo',
'Agencia'
]

orden_cabecera_comentario=[
'NúmeroPedido',
'Validacion de pago'
]
cabecera_comentario = ['NO_PEDIDO', 'ESTADO']