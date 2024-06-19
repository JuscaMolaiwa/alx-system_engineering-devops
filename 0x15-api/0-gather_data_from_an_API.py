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
    url = "https://jsonplaceholder.typicode.com/"

    try:
        employee_id = int(sys.argv[1])  # Convert to int
    except (IndexError, ValueError):
        print("Error: Please provide a valid employee ID (integer).")
        sys.exit(1)

    user_response = requests.get(url + f"users/{employee_id}")

    if user_response.status_code == 200:
        user = user_response.json()

        if user.get("name"):  
            print("Employee Name: OK")  # Explicitly indicate name success

            todos_response = requests.get(url + "todos", params={"userId": employee_id})
            todos = todos_response.json()

            completed = [t.get("title") for t in todos if t.get("completed") is True]

            print(f"Employee {user['name']} is done with tasks({len(completed)}/{len(todos)}):")
            for complete in completed:
                print(f"\t {complete}")

        else:
            print("Employee Name: Incorrect")  # Name missing or incorrect

    else:
        print(f"Error: Unable to fetch user data (status code {user_response.status_code})")
