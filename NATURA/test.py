import json
import time
from pynput import mouse, keyboard
import psutil
import win32gui
import win32process
import win32api
import os

# Variables para contar clics y teclas
clics = 0
teclas = 0
programas = {}
tiempo_inicio = time.time()

# Función para contar clics del ratón
def contar_clicks(x, y, button, pressed):
    global clics
    if pressed:
        clics += 1

# Función para contar teclas presionadas
def contar_teclas(key):
    global teclas
    teclas += 1

# Función para obtener el nombre del programa en la ventana activa
def obtener_programa_activo():
    try:
        hwnd = win32gui.GetForegroundWindow()  # Obtener la ventana activa
        pid = win32process.GetWindowThreadProcessId(hwnd)  # Obtener el PID del proceso asociado
        proceso = psutil.Process(pid[-1])  # Obtener el proceso usando el PID
        ruta_exe = proceso.exe()  # Obtener la ruta del archivo ejecutable
        return obtener_nombre_amigable(ruta_exe)  # Retornar el nombre amigable del programa
    except Exception as e:
        return "Desconocido"

# Función para obtener el nombre amigable del programa
def obtener_nombre_amigable(ruta_exe):
    try:
        # Obtener los metadatos del archivo, incluyendo el ProductName
        info = win32api.GetFileVersionInfo(ruta_exe, '\\')
        nombre_amigable = win32api.GetFileVersionInfo(ruta_exe, '\\StringFileInfo\\040904b0\\ProductName')

        # Si no existe nombre amigable, usar el nombre del archivo
        if not nombre_amigable:
            nombre_amigable = os.path.basename(ruta_exe)

        return nombre_amigable
    except Exception:
        # Si ocurre un error, devolver el nombre del archivo ejecutable como fallback
        return os.path.basename(ruta_exe)

# Función para actualizar la información de los programas activos
def actualizar_informacion_programa():
    programa_actual = obtener_programa_activo()

    if programa_actual not in programas:
        programas[programa_actual] = {
            "tiempoActivo": 0,
            "tiempoInactivo": 0,
            "cantidadClick": 0,
            "cantidadTeclas": 0,
            "tiempoPrimerPlano": 0,
            "tiempoSegundoPlano": 0
        }

    programas[programa_actual]["cantidadClick"] += clics
    programas[programa_actual]["cantidadTeclas"] += teclas

# Función para convertir segundos a horas y minutos
def formatear_tiempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    return f"{horas}h {minutos}m"

# Función para guardar todos los programas en un archivo JSON
def guardar_datos():
    tiempo_total = time.time() - tiempo_inicio

    for programa, data in programas.items():
        # Simula tiempos activo/inactivo, primer plano/segundo plano
        data["tiempoActivo"] = formatear_tiempo(tiempo_total * 0.8)
        data["tiempoInactivo"] = formatear_tiempo(tiempo_total * 0.2)
        data["tiempoPrimerPlano"] = formatear_tiempo(tiempo_total * 0.7)
        data["tiempoSegundoPlano"] = formatear_tiempo(tiempo_total * 0.3)

    # Guarda los datos en un archivo JSON
    with open("actividad_programas.txt", "w") as archivo:
        json.dump(programas, archivo, indent=4)
    print("Datos guardados en 'actividad_programas.txt'")

# Monitorear clics del ratón
listener_mouse = mouse.Listener(on_click=contar_clicks)
listener_mouse.start()

# Monitorear teclas del teclado
listener_keyboard = keyboard.Listener(on_press=contar_teclas)
listener_keyboard.start()

# Mantener el programa activo durante un tiempo y actualizar los datos
try:
    while True:
        actualizar_informacion_programa()  # Actualiza la información cada ciclo
        time.sleep(5)  # Revisa cada 5 segundos
except KeyboardInterrupt:
    print("Programa interrumpido manualmente.")
    guardar_datos()  # Guarda los datos cuando se interrumpe el programa
    listener_mouse.stop()  # Detiene los listeners
    listener_keyboard.stop()
