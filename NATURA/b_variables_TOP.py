from datetime import datetime
# Obtener la fecha actual en formato dd_mm
hoy=datetime.now()
fecha_actual =hoy.strftime('%d.%m')
hoy_carpeta=hoy.strftime('%d_%m')
fecha_dmy=hoy.strftime("%d/%m/%Y")
 


cab_esperada=[
'Agencia',
'No Pedido',
'Orden del Pedidos',
'Código Persona',
'Nombre de la Persona',
'DNI',
'Ciclo',
'Fecha Pedido',
'Fecha Vcto',
'Días de retraso',
'Original',
'Saldo',
'Saldo Corregido',
'Interés/Multa Acumulados',
'% Descuento Saldo',
'% Descuento Interes/Multa',
'Monto Descuento Saldo',
'Monto Descuento Interes/Multa',
'Total Descuentos',
'Monto mínimo a pagar Campaña',
'Estructura Comercial',
'Nombre de la Estructura Comercial',
'Estructura Comercial Padre',
'Nombre de la Estructura Comercial Padre',
'Cod Grupo',
'Fecha nasc',
'Dirección',
'Teléfono Persona',
'Numero Celular',
'Correo Electrónico',
'Tramo Vencimiento',
'Tramo Vencimiento Pedido',
'Riesgo',
'Color',
'Region',
'Fecha de asignación'
# ,
# 'Gestión de la FFVV',
# 'Estado',
# 'Saldo actualizado',
# 'Saldo corregido actualizado',
# 'Días de retraso actualizado'
]

cab_ordenada=[
'Orden del Pedidos',
'Código Persona',
'Cod Grupo',
'Nombre de la Persona',
'NO_HAY_DATA',
'No Pedido',
'NO_HAY_DATA',
'Fecha Pedido',
'Fecha Vcto',
'NO_HAY_DATA',
'Original',
'Saldo',
'Saldo Corregido',
'Interés/Multa Acumulados',
'% Descuento Saldo',
'Monto Descuento Saldo',
'Total Descuentos',
'Monto mínimo a pagar Campaña',
'NO_HAY_DATA',
'NO_HAY_DATA',
'NO_HAY_DATA',
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
'Tramo Vencimiento Pedido',
'Agencia',
'NO_HAY_DATA'   
]

cab_nueva=[
    
]


