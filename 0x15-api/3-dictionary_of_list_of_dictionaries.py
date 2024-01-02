#!/usr/bin/python3
"""
Records all tasks from all employeesand
export to json
"""
if __name__ == '__main__':
    import json
    import requests

    base_url = 'https://jsonplaceholder.typicode.com'
    user_endpoint = f'/users'
    employees = {}

    users = requests.get(base_url + user_endpoint).json()

    for user in users:
        todos_endpoint = f'/users/{user["id"]}/todos'
        todos = requests.get(base_url + todos_endpoint).json()
        tasks = []

        for todo in todos:
            task = {
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed']
            }
            tasks.append(task)
        employees[f'{user["id"]}'] = tasks
    with open(f"todo_all_employees.json", 'w') as f:
        f.write(json.dumps(employees))
