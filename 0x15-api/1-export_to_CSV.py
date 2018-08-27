#!/usr/bin/python3
'''
Takes one argument - Employee's id
Retrieves the number of task Employee has to do and
the tasks that were done

Convert the info to csv file
'''
import csv
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
            else:
                not_done += 1
            task_list.append(task)

    filename = "{}.csv".format(argv[1])

    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in task_list:
            spamwriter.writerow([argv[1], name, task.get('completed'),
                                 task.get('title')])
