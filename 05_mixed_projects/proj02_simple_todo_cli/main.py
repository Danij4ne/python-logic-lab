
"""
Project 02 - Simple TODO CLI

Description:
    Create a simple command-line TODO application that allows the user
    to add, list, and remove tasks during a single program execution.

Requirements:
    - Maintain a list of tasks in memory (no files required).
    - Show a small menu with options such as:
        1. Add a new task
        2. List all tasks
        3. Remove a task by its number or name
        4. Exit
    - Use a loop to keep the program running until the user chooses to exit.
    - Handle invalid options and invalid task selections gracefully.

Notes:
    - Tasks can be simple strings.
    - Focus on list manipulation, input handling, and control flow.

Example (expected behavior):
    === TODO MENU ===
    1. Add task
    2. List tasks
    3. Remove task
    4. Exit

    Select an option: 1
    Enter new task: Buy groceries

    Select an option: 2
    1. Buy groceries
"""

# TODO:
# 1. Create a list to store tasks.
# 2. Display a menu in a loop.
# 3. Implement options to add, list, and remove tasks.
# 4. Handle invalid inputs.
# 5. Exit the program when requested.


tasks = []

while True:
    print("\n=== TODO MENU ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Exit")

    option = input("Select an option: ").strip()

    if option == "1":
        new_task = input("Enter new task: ").strip()
        if new_task:
            tasks.append(new_task)
            print("Task added.")
        else:
            print("Task cannot be empty.")

    elif option == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif option == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            remove_value = input("Enter task number or task name to remove: ").strip()

            if remove_value.isdigit():
                index = int(remove_value) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print(f"Removed: {removed_task}")
                else:
                    print("Invalid task number.")
            else:
                if remove_value in tasks:
                    tasks.remove(remove_value)
                    print(f"Removed: {remove_value}")
                else:
                    print("Task not found.")

    elif option == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option. Please choose between 1 and 4.")