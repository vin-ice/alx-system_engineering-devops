#!/usr/bin/python3
"""Queries reddit fot titles of hottest posts"""
import requests


def top_ten(subreddit):
    """top ten hottest posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Pyscript/1.1"}

    res = requests.get(url=url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        for i in range(10):
            print("{}".format(data['data']["children"][i]['data']['title']))
    else:
        print(None)
