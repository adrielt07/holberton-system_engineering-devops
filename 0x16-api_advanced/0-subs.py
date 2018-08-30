#!/usr/bin/python3
'''
Module name: 0-subs
Number of methods: 1
List of method(s):
   - number_of_subscribers(subreddit_name)
'''
import requests


def number_of_subscribers(subreddit):
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    status = requests.get(url, headers=headers)

    if status.status_code != 200:
        return (0)
    else:
        r = status.json()
        return r['data']['subscribers']
