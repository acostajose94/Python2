from jira import JIRA

jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'
project_key = 'SOP'
issuetype='[System] Service request'
request_type='A1. Carga de Base (Nueva)'
ticket_summary = 'Reportes Historicos'
ticket_description = 'Reportes Historicos'
assignee='jose ivan acosta figueroa'


jira_connection = JIRA(
    basic_auth=(jira_username, jira_token),
    server=jira_url
)


# def get_assignee_id(assignee_name):
#     assignee_id = None
    
#     # Obtener los posibles asignados para el proyecto
#     assignees = jira_connection.search_assignable_users_for_projects('', project_key)
    
#     # Buscar el asignado por nombre
#     for assignee in assignees:
#         if assignee.displayName == assignee_name:
#             assignee_id = assignee.accountId
#             break
    
#     return assignee_id


# assignee_id = get_assignee_id(assignee)
# print('assignee_id '+assignee_id)

def get_issue_type_id(issue_type_name):
    """
    Busca un issuetype por su nombre y devuelve su ID.

    Args:
        issue_type_name (str): El nombre del issuetype a buscar.

    Returns:
        str: El ID del issuetype si se encuentra, o None si no se encuentra.
    """
    issue_types = jira_connection.issue_types()
    for issue_type in issue_types:
        if issue_type.name == issue_type_name:
            return issue_type.id
    return None

issue_type_id=get_issue_type_id(issuetype)
print('issue_type_id '+issue_type_id)


def get_request_type_id(jira_connection, project_key, request_type):
    # Obtener el ID del tipo de solicitud
    request_types = jira_connection.request_types(project_key)
    request_type_id = None
    for rt in request_types:
        if rt.name == request_type:
            request_type_id = rt.id
            break
    return request_type_id

request_type_id=get_request_type_id(jira_connection,project_key,request_type)
print('request_type_id '+request_type_id)


# issue_dict = {
#     'project': {'key': 'SOP'},
#     'summary': ticket_summary,
#     'description': ticket_summary,
#     'issuetype': {'name': issuetype},
# }

# new_issue = jira_connection.create_issue(fields=issue_dict)