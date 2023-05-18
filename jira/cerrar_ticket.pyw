from jira import JIRA

jira_url = 'https://helpdeskavalperu.atlassian.net'
jira_username = 'helpdesk@avalperu.com'
jira_token = 'ATATT3xFfGF0VL-dZkNtEvIXaiHp3I3CgMF754VxGk_wvLtEwIPEd0xIDgAVOEFFD5WikASpWbVQ_4LL_yeMQhELxHHGq3pzu_m5BxaAU1N5GEkVg-Bz6JWOVg2dwExAlarevYGYtG907-Drkeht1bNNSsTx2Akpcfg6JKb24PY4s40Xcog-zJ8=17F533D5'
ticket_summary = 'Reportes Historicos'

jira = JIRA(jira_url, basic_auth=(jira_username, jira_token))
issues = jira.search_issues('summary~"' + ticket_summary + '"', maxResults=1, fields="created")

if len(issues) == 0:
    print('No se encontraron tickets con ese resumen')
else:
    issue = issues[0]
    print('Cerrando ticket', issue.key)
    jira.transition_issue(issue, '961')
