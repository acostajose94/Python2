from jira import JIRA
import datetime
jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'

fecha_hoy     = datetime.date.today().strftime('%Y-%m-%d')
project_key = 'SOP'
ticket_summary = 'BASE UNIQUE Y PAGOS '+fecha_hoy
assignee_name='jose ivan acosta figueroa'
assignee_id='613134836a4c09006aba0f18'
issue_type_id=10002
request_type_id='32'
 
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
    'customfield_10093': {'value': 'UNIQUE'},

}

new_issue = jira_connection.create_issue(fields=issue_dict)

# Imprimir el número del ticket
print(f"El ticket {new_issue.key} ha sido creado exitosamente.")
# Asigna Responsable
fields = {"Responsable": {"accountId": assignee_id}}
new_issue.update(assignee=fields["Responsable"])

# Cambiar el estado del ticket
ticket  = jira_connection.issue(new_issue)
transition_id = jira_connection.find_transitionid_by_name(ticket, 'En curso')
jira_connection.transition_issue(ticket, transition_id)