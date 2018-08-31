#!/usr/bin/python3
'''
Module name: 2-recurse
Has one method:
 - recurse(subreddit, hot_list=[])
'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''
    function that queries the Reddit API and returns the list of all hot
    articles

    - If the subreddit does not exists, return None
    Usage:
       recurse(programming)
       returns a list of all articles
    '''
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    if after is not None:
        url = "{}/?after={}".format(url, after)
    headers = {'user-agent': 'my-app/0.0.1'}
    status = requests.get(url, allow_redirects=False, headers=headers)
    if status.status_code != 200:
        return None
    r = status.json()

    if 'data' in r:
        for item in r['data']['children']:
            hot_list.append(item['data']['title'])
    else:
        return hot_list

    if r['data']['after'] is None:
        return hot_list
    else:
        recurse(subreddit, hot_list, r['data']['after'])
        return hot_list
