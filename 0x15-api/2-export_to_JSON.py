#!/usr/bin/python3
'''
Takes one argument - Employee's id
Retrieves the number of task Employee has to do and
the tasks that were done

Convert the info to csv file
'''
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_url = 'http://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    user_info = requests.get(user_url).json()
    tasks_url = 'http://jsonplaceholder.typicode.com/todos'
    tasks_info = requests.get(tasks_url).json()
    task_list = []
    new_list = []
    username = user_info.get('username')
    new_dict = {}

    for task in tasks_info:
        if task.get('userId') == int(argv[1]):
            task_list.append(task)

    filename = "{}.json".format(argv[1])
    for task in task_list:
        new_dict["task"] = task.get('title')
        new_dict["completed"] = task.get('completed')
        new_dict["username"] = username
        new_list.append(new_dict)
        new_dict = {}
    output = {}
    output[str(argv[1])] = new_list
    with open(filename, 'w') as outfile:
        json.dump(output, outfile)
