import requests

request = requests.Session()

jira_url = 'https://issues.apache.org/jira/rest/api/2/search'


def jira_issue_count(jira_name, gather_start_time=None):
    """
    获取jira issue总数（从gather_start_time时间点开始收集）

    :param jira_name: jira 名称
    :param gather_start_time: 开始收集时间
    :return: 总数
    """
    if gather_start_time:
        jql = 'project = {} AND created >= "{}"'.format(jira_name, gather_start_time)
    else:
        jql = 'project = {}'.format(jira_name)
    data = {
        'jql': jql,
        'fields': ['id', 'key']
    }
    response = request.post(url=jira_url, json=data)
    interface_data = response.json()
    print('[{}] total num: {}'.format(jira_name, interface_data.get('total')))


if __name__ == '__main__':
    jira_issue_count('AMQ')
    jira_issue_count('AMQ', '2022-12-01 00:00')
