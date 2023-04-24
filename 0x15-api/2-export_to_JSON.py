#!/usr/bin/python3
"""REST api consumer/client that writes to json file"""
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

            dump = {id: [{"task": t.get("title"),
                          "completed": t.get("completed"),
                          "username": username} for t in todos]}

            with open("{}.json".format(id), "w", encoding="utf8") as f:
                f.write(dumps(dump))
