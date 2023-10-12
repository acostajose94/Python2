archivo_excel = 'AVAL_TLS_PREGRADO NO VIGENTE al 260523.xlsx'

# Obtener el índice de inicio del texto deseado
indice_inicio = archivo_excel.find('AVAL_TLS_PREGRADO') + len('AVAL_TLS_PREGRADO')

# Seleccionar todo el texto después de 'AVAL_TLS_PREGRADO'
texto_seleccionado = archivo_excel[indice_inicio:]

print(texto_seleccionado)  # Salida: ' NO VIGENTE al 260523.xlsx'
