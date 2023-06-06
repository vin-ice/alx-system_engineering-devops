#!/usr/bin/python3
"""Queries reddit for articles of a subreddit"""
import requests
from time import sleep


def count_parse(symbols, data_list):
    """Counts instance of each symbol in data"""
    data = []
    if isinstance(symbols, list):
        symbols = {s: 0 for s in symbols}
    for line in data_list:
        data = [w.strip().lower() for w in line.split()]
        for word in data:
            if word in symbols.keys():
                symbols[word] += 1
    return symbols


def count_words(subreddit, word_list=[], cursor=None):
    """hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Pyscript/2.1"}
    params = {"limit": 100}

    if cursor:
        params["after"] = cursor
    res = requests.get(url=url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        cursor = data["data"]["after"]
        target = data["data"]["children"]
        title_list = [t["data"]["title"] for t in target]

        word_list = count_parse(word_list, title_list)

        if cursor is None:
            for k, v in word_list.items():
                print("{}: {}".format(k, v))
        else:
            sleep(5)
            return count_words(subreddit, word_list=word_list, cursor=cursor)

    else:
        return None
