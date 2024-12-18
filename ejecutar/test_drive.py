import subprocess
import time
import pyautogui
import os

# Definir la ruta de Chrome y la URL de destino
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
profile = r"--profile-directory=Profile 3"
url = "https://drive.google.com/drive/folders/19U0E1FrynnQgp77XS2LtJryzDABwCx9I?pli=1"

# Abrir Chrome con el perfil específico y cargar la URL
subprocess.Popen([chrome_path, profile, url])

# Esperar 5 segundos para que la página cargue completamente
time.sleep(5)

# Obtener el tamaño de la pantalla
screen_width, screen_height = pyautogui.size()

# Calcular las coordenadas del centro
center_x = screen_width / 2
center_y = screen_height / 2

# Hacer clic en el centro de la pantalla para asegurar que Google Drive está enfocado
pyautogui.click(center_x, center_y)

# Esperar un momento para que el clic sea registrado
time.sleep(1)

# Abrir el explorador de archivos en el escritorio
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.startfile(desktop_path)

# Esperar un momento para que el explorador de archivos se abra
time.sleep(3)

# Obtener las coordenadas de la carpeta a copiar (ajusta estas coordenadas según sea necesario)
# Usaremos coordenadas estimadas, ajústalas según sea necesario
folder_x, folder_y = 200, 300  # Coordenadas aproximadas de la carpeta en el escritorio

# Hacer clic y arrastrar la carpeta desde el explorador de archivos a la ventana de Google Drive
pyautogui.moveTo(folder_x, folder_y)
pyautogui.mouseDown()
pyautogui.moveTo(center_x, center_y, duration=2)  # Mover al centro de la pantalla (ventana de Google Drive)
pyautogui.mouseUp()

# Esperar un momento para que la carga se inicie
time.sleep(3)

print("Proceso completado.")
