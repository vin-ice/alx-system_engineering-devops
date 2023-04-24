#!/usr/bin/python3
"""REST api consumer/client"""
from json import dumps
import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com/"
if __name__ == "__main__":
    res = requests.get(url="".join([URL, "users/"]))
    if res.status_code == 200:
        ids = [str(u.get("id")) for u in res.json()]
        usernames = [u.get("username") for u in res.json()]
        todos = [requests.get(url="".join([URL, "users/", (id),
                                          "/todos"])).json()
                 for id in ids]

        dump = {ids[i]: [{"username": usernames[i],
                          "task": t.get("title"),
                          "completed": t.get("completed")}
                         for t in todos[i]] for i in range(len(ids))}

        with open("todo_all_employees.json", "a", encoding="utf8") as f:
            f.write(dumps(dump, indent=4))
