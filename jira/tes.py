from jira import JIRA

jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'
project_key = 'SOP'
issuetype_name='[System] Service request'
request_type_name='E3. Reporte - Actualizacion en Diseno de Reporte'
ticket_summary = 'Reportes Historicos'
# ticket_description = 'Reportes Historicos'
assignee_name='jose ivan acosta figueroa'

assignee_id='613134836a4c09006aba0f18'
issue_type_id=10002
request_type_id='55'
 

jira = JIRA(
    basic_auth=(jira_username, jira_token),
    server=jira_url
)
# Fetch all fields
allfields = jira.fields()

# Make a map from field name -> field id
nameMap = {field['name']:field['id'] for field in allfields}

# for a in nameMap:
#     print(a)    
# Fetch an issue
issue = jira.issue('SOP-11839')


getvalue = getattr(issue.fields, nameMap["Request Type"])
print(getvalue)