from jira import JIRA

jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'
ticket_summary = 'Reportes Historicos'

jira= JIRA(
    basic_auth=(jira_username, jira_token),
    server=jira_url
)

# obtener los campos disponibles para el proyecto SOP
issue  = jira.issue('SOP-11345')

    
field_list = issue.fields

# Convertir el objeto PropertyHolder en una lista
field_list = list(field_list)

# Imprimir los nombres de los campos
for field_name in field_list:
    print(field_name)