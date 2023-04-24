#!/usr/bin/python3
"""REST api consumer/client that prints  an employee's completed tasks"""
import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com/"
if __name__ == "__main__":
    if not len(argv) < 2:
        id = str(argv[1])

        res = requests.get(url="".join([URL, "users/", id]))
        if res.status_code == 200:
            name = res.json().get("name")
            todos = requests.get(url="".join([URL, "users/", id,
                                 "/todos"])).json()
            tasks = list(filter(lambda t: t["completed"] == True, todos))

            print("Employee {} is done with tasks ({}/{}):"
                  .format(name, len(tasks), len(todos)))
            for task in tasks:
                print("\t {}".format(task.get("title")))
