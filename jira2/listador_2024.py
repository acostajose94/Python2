from jira import JIRA
jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'

# Conectar a Jira
jira = JIRA(basic_auth=(jira_username, jira_token), server=jira_url)

# Obtener metadatos del proyecto y campos
project_key = 'SOP'
issue_type = '10002'  # Reemplaza con el tipo de issue que estés utilizando

# Obtener metadatos del campo específico
metadata = jira.editmeta(issue_type)

# Ver las opciones del campo customfield_10010
custom_field_options = metadata['fields']['customfield_10010']['allowedValues']

# Imprimir las opciones disponibles
for option in custom_field_options:
    print(option['value'])
