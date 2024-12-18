from jira import JIRA

jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'
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

issue_dict = {
    'project': {'key': 'SOP'},
    'summary': ticket_summary,
    'description': ticket_summary,
    'issuetype': {'name': issuetype},
}

new_issue = jira_connection.create_issue(fields=issue_dict)