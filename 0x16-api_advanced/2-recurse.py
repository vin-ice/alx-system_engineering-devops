#!/usr/bin/python3
"""Queries reddit fot articles of a subreddit"""
import requests


def recurse(subreddit, hot_list=[], cursor=None):
    """top ten hottest posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Pyscript/2.1"}
    params = {"limit": 100}

    if cursor:
        params["after"] = cursor

    res = requests.get(url=url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        posts = data["data"]["children"]
        if not posts:
            return hot_list
        hot_list.extend([post['data']['title'] for post in posts])
        cursor = data['data']['after']
        if cursor is None:
            return hot_list
        return recurse(subreddit, hot_list=hot_list, cursor=cursor)
    else:
        return None
