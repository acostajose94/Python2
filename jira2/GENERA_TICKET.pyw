import tkinter as tk
from tkinter import ttk
from jira import JIRA
import random
import time
import datetime
import threading  # Para manejar los hilos

jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'

# Función para crear y cerrar ticket
def gestionar_ticket():
    # Obtener los valores seleccionados en la interfaz
    empresa = empresa_var.get()
    request_type = request_type_var.get()
    
    # Verificar qué tipo de request es
    request_type_id = ''
    if request_type == 'REPORTES':
        request_type_id = '55'
    elif request_type == 'PAGO':
        request_type_id = '31'
    elif request_type == 'BASE':
        request_type_id = '32'
    elif request_type == 'BASE y PAGOS':
        request_type_id = '32'
    elif request_type == 'SALDO':
        request_type_id = '31'
    elif request_type == 'Efectividades':
        request_type_id = '55'



    # Generar fecha y ticket summary
    fecha_hoy = datetime.date.today().strftime('%m-%d')
    
    project_key = 'SOP'
    ticket_summary = f'{request_type} {empresa} {fecha_hoy}'
    assignee_id = '10225'
    assignee_name = 'Jose Acosta'
    issue_type_id = 10002
    
    # Conectar a JIRA
    jira_connection = JIRA(basic_auth=(jira_username, jira_token), server=jira_url)

    # Crear el ticket
    issue_dict = {
        'project': {'key': project_key},
        'summary': ticket_summary,
        'description': ticket_summary,
        'issuetype': {'id': issue_type_id},
        'customfield_10010': request_type_id,
        'customfield_10085': [{'id': '10225', 'value': 'Jose Acosta'}],
        'customfield_10093': {'value': empresa},
    }

    new_issue = jira_connection.create_issue(fields=issue_dict)
    print(f"El ticket {new_issue.key} ha sido creado exitosamente.")

    # Cambiar el estado a "En curso"
    ticket = jira_connection.issue(new_issue)
    transition_id = jira_connection.find_transitionid_by_name(ticket, 'En curso')
    jira_connection.transition_issue(ticket, transition_id)

    # Esperar entre 7 y 11 minutos antes de cerrar el ticket
    random_minutes = random.uniform(7, 11)
    print(f"Esperando {random_minutes:.2f} minutos para cerrar el ticket...")
    time.sleep(random_minutes * 60)

    # Cerrar el ticket
    ticket_phrase = f'{request_type} {empresa}'
    issues_c = jira_connection.search_issues(f'summary ~ "{ticket_phrase}"', maxResults=1, fields="created")

    if len(issues_c) == 0:
        print('No se encontraron tickets con esa frase parcial')
    else:
        issue = issues_c[0]
        print(f'Cerrando ticket {issue.key}')
        jira_connection.transition_issue(issue, '961')  # ID de transición para cerrar el ticket
        print("El ticket ha sido cerrado.")

# Función que ejecuta la gestión del ticket en un hilo
def gestionar_ticket_en_hilo():
    ticket_thread = threading.Thread(target=gestionar_ticket)
    ticket_thread.start()

# Configurar la interfaz de usuario
root = tk.Tk()
root.title("Gestión de Tickets JIRA")

# Variables para los dropdowns
empresa_var = tk.StringVar()
request_type_var = tk.StringVar()

# Etiquetas y campos
ttk.Label(root, text="Seleccione la empresa:").grid(row=0, column=0, padx=10, pady=10)
empresa_combo = ttk.Combobox(root, textvariable=empresa_var, state='readonly')  # readonly para evitar escritura
empresa_combo['values'] = ('NATURA', 'UNIQUE', 'ALFIN BANCO')
empresa_combo.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Seleccione el tipo de solicitud:").grid(row=1, column=0, padx=10, pady=10)
request_type_combo = ttk.Combobox(root, textvariable=request_type_var, state='readonly')  # readonly para evitar escritura
request_type_combo['values'] = ('SALDO', 'PAGO', 'BASE','BASE y PAGOS', 'REPORTES','Efectividades')
request_type_combo.grid(row=1, column=1, padx=10, pady=10)

# Botón para gestionar ticket
ttk.Button(root, text="Crear y cerrar ticket", command=gestionar_ticket_en_hilo).grid(row=2, columnspan=2, pady=20)

# Iniciar la interfaz
root.mainloop()
