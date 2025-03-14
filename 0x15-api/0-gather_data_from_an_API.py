#!/usr/bin/python3
"""This script will return the to-do list info for an employee ID."""
import requests
from sys import argv
""" and then run a request module used to fetch the url response"""


def get_employee_todo_progress(employee_id):
    """this is the  employee to do progress function"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_datas = requests.get(url + f"users/{employee_id}")
        user_data = user_datas.json()
        employee_name = user_data['name']

        """run a fetch for  the todos list for an employee
        using todos?<dic_key>=value"""
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        json_todos_list = todos_list.json()

        """calculate the task done and left undone"""
        total_task = len(json_todos_list)
        """check the completed tasks"""
        task_done = [task for task in json_todos_list if task['completed']]
        no_task_done = len(task_done)

        """display all results"""
        print(f"Employee {employee_name} is done with tasks("
              f"{no_task_done}/{total_task}):")
        """printing the title of completed task"""
        for task in task_done:
            print(f"\t {task['title']}")
    except Exception as e:
        print(f"an error occured: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <emplyee_id>")
    else:
        get_employee_todo_progress(argv[1])
