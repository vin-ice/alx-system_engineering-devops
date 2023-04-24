#!/usr/bin/python3
"""REST api consumer/client"""
import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com/"
if __name__ == "__main__":
    if not len(argv) < 2:
        id = str(argv[1])

        res = requests.get(url="".join([URL, "users/", id]))
        if res.status_code == 200:
            name = res.json().get("username")
            todos = requests.get(url="".join([URL, "users/", id,
                                 "/todos"])).json()

            with open("{}.csv".format(id), "a", encoding="utf8") as f:
                for todo in todos:
                    f.write("\"{}\",\"{}\",\"{}\",\"{}\"\n"
                            .format(id, name, todo.get("completed"),
                                    todo.get("title")))
