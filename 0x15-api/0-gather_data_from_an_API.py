#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    base_url = 'https://jsonplaceholder.typicode.com'
    user_endpoint = f'/users/{argv[1]}'
    todos_endpoint = f'/users/{argv[1]}/todos'

    user = requests.get(base_url + user_endpoint).json()
    todos = requests.get(base_url + todos_endpoint).json()
    done = [x for x in todos if x['completed'] is True]
    print(f"Employee {user['name']} " +
          f"is done with tasks({len(done)}/{len(todos)}):")
    for todo in done:
        print(f"\t {todo['title']}")
