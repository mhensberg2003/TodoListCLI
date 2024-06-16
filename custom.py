def add_task(task, todo_file_path):
    # Opens file and appends the task to the end
    with open(todo_file_path, "a") as file:
        file.write(task + "\n")


def remove_task(todo_file_path):
    # Opens file and checks if list is empty
    with open(todo_file_path, 'r+') as file:
        lines = file.readlines()
        if not lines:
            print("The to-do list is empty.")
            return

        # Display the tasks with an index
        for i, line in enumerate(lines):
            print(f"({i}) {line.strip()}")

        # Get the user's selection for the task to remove
        try:
            selection = int(input("Please select the task you want to remove (by number): "))
            if selection < 0 or selection >= len(lines):
                print("Invalid selection. Please try again.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        # Remove the selected task from the list
        del lines[selection]

        # Truncate the file and write the updated list back to the file
        file.seek(0)
        file.truncate()
        file.writelines(lines)

        print("Task removed successfully.")


def view_all_tasks(todo_file_path):
    # Opens file, reads it, and then displays it
    with open(todo_file_path, "r") as file:
        fileread = file.read().strip()

        if fileread == "":
            print("No tasks to do!")
        else:
            print(fileread)
