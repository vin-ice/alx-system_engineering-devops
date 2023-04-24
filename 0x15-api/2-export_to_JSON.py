#!/usr/bin/python3
"""REST api consumer/client"""
from json import dumps
import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com/"
if __name__ == "__main__":
    if not len(argv) < 2:
        id = str(argv[1])

        res = requests.get(url="".join([URL, "users/", id]))
        if res.status_code == 200:
            name = res.json().get("name")
            username = res.json().get("username")
            todos = requests.get(url="".join([URL, "users/", id,
                                 "/todos"])).json()

            with open(f"{id}.json", "a", encoding="utf8") as f:
                f.write(dumps({id: [{"task": t.get("title"),
                                     "completed": t.get("completed"),
                                     "username": username} for t in todos]},
                              indent=4))
