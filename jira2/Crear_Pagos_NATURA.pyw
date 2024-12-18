from jira import JIRA
import datetime
import time
import random

jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'

fecha_hoy     = datetime.date.today().strftime('%Y-%m-%d')
fecha_actual = datetime.datetime.now()
ayer=fecha_actual- datetime.timedelta(days=1)
if fecha_actual.weekday() == 0:
    fecha_hoy = fecha_hoy + '/' + ayer.strftime('%d')
project_key = 'SOP'
ticket_summary = 'PAGOS NATURA '+fecha_hoy
assignee_name='Jose Acosta'
assignee_id='10225'
issue_type_id=10002
#PAGO ID
request_type_id='31'
 
jira_connection = JIRA(
    basic_auth=(jira_username, jira_token),
    server=jira_url
)

issue_dict = {
    'project': {'key': project_key},
    'summary': ticket_summary,
    'description': ticket_summary,
    'issuetype': {'id': issue_type_id},
    'customfield_10010': request_type_id,
    'customfield_10085': [{'id': '10225', 'value': 'Jose Acosta'}],
    'customfield_10093': {'value': 'NATURA'},

}

new_issue = jira_connection.create_issue(fields=issue_dict)

# Imprimir el número del ticket
print(f"El ticket {new_issue.key} ha sido creado exitosamente.")

# Cambiar el estado del ticket
ticket  = jira_connection.issue(new_issue)
transition_id = jira_connection.find_transitionid_by_name(ticket, 'En curso')
jira_connection.transition_issue(ticket, transition_id)



random_minutes = random.uniform(4, 6)
# Esperar 4 minutos antes de cerrar el ticket
print("Esperando 4 minutos para cerrar el ticket...")
time.sleep(random_minutes * 60) # 4 minutos en segundos

# Cerrar el ticket
# Primero obtienes el ticket y luego realizas la transición de cierre
ticket_phrase = 'PAGOS NATURA'
issues_c = jira_connection.search_issues(f'summary ~ "{ticket_phrase}"', maxResults=1, fields="created")

if len(issues_c) == 0:
    print('No se encontraron tickets con esa frase parcial')
else:
    issue = issues_c[0]
    print(f'Cerrando ticket {issue.key}')
    jira_connection.transition_issue(issue, '961')  # '961' es el ID de la transición a cerrar el ticket

print("El ticket ha sido cerrado.")


 