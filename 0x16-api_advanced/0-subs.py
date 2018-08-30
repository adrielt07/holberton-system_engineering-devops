#!/usr/bin/python3
'''
Module name: 0-subs
Number of methods: 1
List of method(s):
   - number_of_subscribers(subreddit_name)
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Retrieves number of subscribers to a subreddit
    - If the subreddit does not exists, return 0
    Usage:
       number_of_subscribers(programming)
       Returns the number of subscribers the 'programming' subreddit has
    '''
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    status = requests.get(url, headers=headers)

    if status.status_code != 200:
        return (0)
    else:
        r = status.json()
        return r['data']['subscribers']
