#!/usr/bin/python3
"""
For a given employee ID,
Records all tasks that are owned by this employee
and export to CSV
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    user_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    user_endpoint = f'/users/{user_id}'
    todos_endpoint = f'/users/{user_id}/todos'

    user = requests.get(base_url + user_endpoint).json()
    todos = requests.get(base_url + todos_endpoint).json()
    with open(f"{user_id}.csv", 'w') as f:
        for todo in todos:
            f.write(f'"{user_id}","{user["username"]}",' +
                    f'"{todo["completed"]}","{todo["title"]}"\n')
