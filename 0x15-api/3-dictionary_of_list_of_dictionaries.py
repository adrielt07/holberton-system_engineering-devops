#!/usr/bin/python3
'''
Takes one argument - Employee's id
Retrieves the number of task Employee has to do and
the tasks that were done

Convert the info to csv file
'''
import json
import requests

if __name__ == '__main__':
    user_url = 'http://jsonplaceholder.typicode.com/users'
    user_info = requests.get(user_url).json()
    tasks_url = 'http://jsonplaceholder.typicode.com/todos'
    tasks_info = requests.get(tasks_url).json()
    new_list = []
    new_dict = {}
    all_todo = {}

    for user in user_info:
        for task in tasks_info:
            if task.get('userId') == user.get('id'):
                new_dict["task"] = task.get('title')
                new_dict["completed"] = task.get('completed')
                new_dict["username"] = user.get('username')
                new_list.append(new_dict)
                new_dict = {}
        all_todo[user.get('id')] = new_list
        new_list = []
    with open("todo_all_employees.json", 'w') as outfile:
        json.dump(all_todo, outfile)
