import datetime

hoy=datetime.datetime.now()
fecha_oin=hoy.strftime('%d.%m.%y')
fecha_actual =hoy.strftime('%d_%m')

nombre_columna = "SAP_CODE"
cantidad_columnas = 2

# arch1='AVAL DEUDORES CERTUS_PREGRADO NO VIGENTE 12.06.23.xlsx'
# arch2='AVAL DEUDORES CERTUS_PREGRADO VIGENTE 12.06.23.xlsx'
# archivos_excel=[arch1,arch2]
# Carpeta de destino
destino_retirar = r'V:\Excel\\'

# Definir la cabecera esperada
cabecera_esperada = ['PERIODO', 'CODIGO_ALUMNO', 'TIPO_DOCUMENTO', 'NUMERO_DOCUMENTO', 'NOMBRES', 'APELLIDOS',
                    'EMAIL_INSTITUCIONAL', 'EMAIL_PERSONAL', 'TELEFONO_CELULAR', 'TELEFONO_FIJO', 'DISTRITO',
                    'DIRECCION', 'REF_DIRECCION', 'DEPARTAMENTO', 'PROVINCIA', 'CICLO', 'TIPO_ALUMNO',
                    'NIVEL_CODE', 'CARRERA_CODE', 'CARRERA', 'SEDE', 'TURNO', 'SECCION',
                    'ESTADO_MATR_CICLO_CODE', 'FECHA_RETIRO_CICLO', 'MOTIVO_RETIRO', 'ULTIMA_ASISTENCIA',
                    'NUMERO_TRANSACCION', 'CODIGO_DE_DETALLE', 'CODIGO_DETALLE_DESC', 'FECHA_VENCIMIENTO',
                    'FECHA_EMISION', 'TIPO_DOC', 'SERIE_COMPROBANTE', 'NUMERO_COMPROBANTE', 'IMPORTE', 'CARGO',
                    'REVERSIONES', 'DESCUENTOS', 'CANCELACIONES', 'NOTAS_CREDITO', 'PAGOS', 'SALDO',
                    'IMPORTE_OBSERVADO', 'DEF_FUN_OK', 'SAP_CODE', 'COD. DUPL',	'EXT HBC'

                    ]


nueva_cabecera =    [
                    "PERIODO", "CODIGO_ALUMNO", "TIPO_DOCUMENTO", "NUMERO_DOCUMENTO", "NOMBRES",
                    "APELLIDOS", "EMAIL_INSTITUCIONAL", "EMAIL_PERSONAL", "TELEFONO_CELULAR",
                    "TELEFONO_FIJO", "DISTRITO", "DIRECCION", "REF_DIRECCION", "DEPARTAMENTO",
                    "PROVINCIA", "CICLO", "TIPO_ALUMNO", "NIVEL_CODE", "CARRERA_CODE", "CARRERA",
                    "SEDE", "TURNO", "SECCION", "ESTADO_MATR_CICLO_CODE", "FECHA_RETIRO_CICLO",
                    "MOTIVO_RETIRO", "ULTIMA_ASISTENCIA", "NUMERO_TRANSACCION", "CODIGO_DE_DETALLE",
                    "CODIGO_DETALLE_DESC", "FECHA_VENCIMIENTO", "FECHA_EMISION", "TIPO_DOC",
                    "SERIE_COMPROBANTE", "NUMERO_COMPROBANTE", "IMPORTE", "CARGO", "REVERSIONES",
                    "DESCUENTOS", "CANCELACIONES", "NOTAS_CREDITO", "PAGOS", "SALDO",
                    "IMPORTE_OBSERVADO", "DEF_FUN_OK", "UNICO_ALUMNOS", "SALDO_CERO",
                    "RAPACTACIONES", "AGENCIAS"
                    ]
