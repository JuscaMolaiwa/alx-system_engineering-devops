#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    """Fetches and displays an employee's to-do list progress.

    Args:
        employee_id (int): The ID of the employee.
    """
    try:
        # Fetch user information
        user_response = requests.get(f"{API_URL}/users/{employee_id}")
        user_response.raise_for_status()  # Raise an exception for HTTP errors
        user = user_response.json()
        employee_name = user["name"]

        # Fetch to-do list
        todos_response = requests.get(f"{API_URL}/todos", params={"userId": employee_id})
        todos_response.raise_for_status()
        todos = todos_response.json()

        completed_tasks = [task["title"] for task in todos if task["completed"]]

        # Display progress summary
        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todos)}):")

        # Display completed task titles
        for task_title in completed_tasks:
            print(f"\t {task_title}")
        

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"Unexpected data format: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please provide an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
