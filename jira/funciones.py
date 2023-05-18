from jira import JIRA


def get_assignee_id(assignee_name,jira_connection):
    assignee_id = None
    
    # Obtener los posibles asignados para el proyecto
    assignees = jira_connection.search_assignable_users_for_projects('', project_key)
    
    # Buscar el asignado por nombre
    for assignee in assignees:
        if assignee.displayName == assignee_name:
            assignee_id = assignee.accountId
            break
    
    return assignee_id