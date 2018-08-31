#!/usr/bin/python3
'''
Module name: 1-top-ten
Has one method:
 - top_ten(subreddit)
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.

    - If the subreddit does not exists, print and return None
    Usage:
       number_of_subscribers(programming)
       Returns the top ten posts for a given subreddit
    '''
    url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
    if after is not None:
        url = "{}&after={}".format(url, after)
    headers = {'user-agent': 'my-app/0.0.1'}
    status = requests.get(url, allow_redirects=False, headers=headers)

    if status.status_code != 200:
        return None

    r = status.json()
    if 'children' in r['data']:
        for item in r['data']['children']:
            hot_list.append(item['data']['title']
