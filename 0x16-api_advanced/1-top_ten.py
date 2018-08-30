#!/usr/bin/python3
'''
Module name: 1-top-ten
Has one method:
 - top_ten(subreddit)
'''
import requests


def top_ten(subreddit):
    '''
    function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.

    - If the subreddit does not exists, print and return None
    Usage:
       number_of_subscribers(programming)
       Returns the top ten posts for a given subreddit
    '''
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    status = requests.get(url, allow_redirects=False, headers=headers)

    if status.status_code != 200:
        print("None")
        return None

    r = status.json()

    num = len(r['data']['children'])
    if num > 10:
        num = 10
    count = 0
    for item in r['data']['children']:
        if count == num:
            break
        else:
            print(item['data']['title'])
        count += 1
