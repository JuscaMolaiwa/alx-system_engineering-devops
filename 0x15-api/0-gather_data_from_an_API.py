#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.

Original code from: [original source, e.g., "https://jsonplaceholder.typicode.com"]
"""

import requests
import sys

def fetch_user_data(employee_id):
    """
    Fetches user information for a given employee ID.
    
    Args:
    employee_id (str): The ID of the employee
    
    Returns:
    dict: User information
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()

def fetch_todo_data(employee_id):
    """
    Fetches to-do list for a given employee ID.
    
    Args:
    employee_id (str): The ID of the employee
    
    Returns:
    list: List of to-do items
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": employee_id}
    response = requests.get(url, params=params)
    return response.json()

def main():
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user and to-do data
    user = fetch_user_data(employee_id)
    todos = fetch_todo_data(employee_id)

    # Filter completed tasks
    completed_tasks = [task['title'] for task in todos if task['completed']]

    # Output the result
    print(f"Employee {user.get('name')} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    main()
