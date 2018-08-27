#!/usr/bin/python3
'''
Takes one argument - Employee's id
Retrieves the number of task Employee has to do and
the tasks tha were done
'''
import requests
from sys import argv

if __name__ == '__main__':
    user_url = 'http://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    user_info = requests.get(user_url).json()
    tasks_url = 'http://jsonplaceholder.typicode.com/todos'
    tasks_info = requests.get(tasks_url).json()
    done = 0
    not_done = 0
    task_list = []
    name = user_info.get('name')

    for task in tasks_info:
        if task.get('userId') == int(argv[1]):
            if task.get('completed') is True:
                done += 1
                task_list.append(task.get('title'))
            else:
                not_done += 1
    total = done + not_done

    first_line = "Employee {} is done with tasks({}/{}):".format(name,
                                                                 done, total)

    print(first_line)
    for task in task_list:
        print("\t{}".format(task))
