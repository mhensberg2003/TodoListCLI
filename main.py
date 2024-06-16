# Importing necessary modules
from custom import add_task, remove_task, view_all_tasks
from os import path
from time import sleep

# Set your wanted file name
todo_file_name = "todo_list.txt"

if not(path.isfile(todo_file_name)):
    open(todo_file_name, "x")

while True:
    print("Welcome to the to-do planner...")
    sleep(1)
    selection = input("Please select what you want to do:"
          "\n(1) Add a task"
          "\n(2) Remove a task"
          "\n(3) View all tasks"
          "\n(4) Exit\n")

    if selection == "1":
        task = input("What task do you want to add?: ")
        add_task(task, "todo_list.txt")

    elif selection == "2":
        remove_task("todo_list.txt")

    elif selection == "3":
        view_all_tasks("todo_list.txt")

    elif selection == "4":
        print("Goodbye!")
        sleep(1)
        break
    else:
        print("Please input a valid number!")
        sleep(1)
        continue

