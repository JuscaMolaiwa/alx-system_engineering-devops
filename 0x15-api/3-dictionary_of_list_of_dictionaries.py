#!/usr/bin/python3
"""
Returns to-do list information for all employees.

This script fetches the user information and to-do lists for all employees
from the JSONPlaceholder API. It then exports the data to a JSON file.
"""

import json
import requests


def fetch_all_todo_lists():
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users = requests.get(url + "users").json()

    # Fetch all todos
    todos = requests.get(url + "todos").json()

    # Organize todos by user
    todo_dict = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todo_dict[user_id] = []
        for todo in todos:
            if todo.get("userId") == user_id:
                todo_dict[user_id].append({
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })

    # Write to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todo_dict, json_file)


if __name__ == "__main__":
    fetch_all_todo_lists()
