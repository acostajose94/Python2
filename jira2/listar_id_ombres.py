from jira import JIRA

jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'
ticket_summary = 'Reportes Historicos'

project_key = 'SOP'
issuetype='[System] Service request'
request_type='E3. Reporte - Actualizacion en Diseno de Reporte'
ticket_summary = 'Reportes Historicos'
ticket_description = 'Reportes Historicos'
assignee='jose ivan acosta figueroa'



jira_connection = JIRA(
    basic_auth=(jira_username, jira_token),
    server=jira_url
)



# Obtener el ID del tipo de solicitud
request_types = jira_connection.request_types(project_key)
request_type_id = None
for rt in request_types:
    if rt.name == request_type:
        request_type_id = rt.id
        break

print('----------'+request_type_id)


fields = jira_connection.fields()
for field in fields:
    if "customfield_" in field["id"]:
        print("ID " + field["id"]+" Nombre " + field["name"])

# # Crear el diccionario de datos del ticket
# issue_dict = {
#     'project': {'key': project_key},
#     'summary': ticket_summary,
#     'description': ticket_description,
#     'issuetype': {'id': issue_type_id},
#     'customfield_12345': {'id': request_type_id},
#     'assignee': {'name': assignee_id}
# }

# # Crear el ticket en JIRA
# new_issue = jira_connection.create_issue(fields=issue_dict)

# # Imprimir el ID del ticket creado
# print('Se ha creado el ticket con ID:', new_issue.key)