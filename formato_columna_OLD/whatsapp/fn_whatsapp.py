from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def enviar_mensaje_whatsapp_grupo(mensaje, grupo_nombre):
    # Ruta al controlador de Selenium (chromedriver)
    webdriver_path = r'C:\chromedriver_win32\\chromedriver'  # Reemplaza 'ruta_al_controlador' por la ruta correcta
    
    # Inicializar el controlador de Selenium
    driver = webdriver.Chrome(webdriver_path)
    
    # Abrir WhatsApp Web
    driver.get('https://web.whatsapp.com/')
    
    # Esperar a que el usuario escanee el código QR
    input('Escanea el código QR y presiona Enter para continuar...')
    
    # Buscar el grupo por su nombre
    grupo_xpath = f'//span[@title="{grupo_nombre}"]'
    grupo = driver.find_element_by_xpath(grupo_xpath)
    
    # Abrir el grupo
    grupo.click()
    
    # Esperar un poco para asegurarnos de que se haya abierto el grupo
    time.sleep(2)
    
    # Encontrar el cuadro de texto para escribir el mensaje
    cuadro_texto = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    
    # Escribir el mensaje
    cuadro_texto.send_keys(mensaje)
    
    # Enviar el mensaje
    cuadro_texto.send_keys(Keys.ENTER)
    
    # Cerrar el controlador de Selenium
    driver.quit()
