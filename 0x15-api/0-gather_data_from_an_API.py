#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Getting the employee information using the provided employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Getting the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filtering the  completed tasks and counting them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Printing the employee's name and the number of the completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one by one with the indentation
    [print("\t {}".format(complete)) for complete in completed]
