
"""
Project 01 - Text Menu Application

Description:
    Create a simple console-based menu system that allows the user
    to select from multiple options and perform basic actions.

Requirements:
    - Display a menu with several numbered options (e.g., 1, 2, 3...).
    - Use a loop to keep the menu running until the user chooses to exit.
    - Handle invalid menu selections gracefully.
    - Implement at least three actions, such as:
        - Printing a message
        - Performing a simple calculation
        - Showing a list of items
    - Include an option to exit the program.

Notes:
    - User input is required for menu selections.
    - The focus is on control flow, loops, and program structure.

Example (expected behavior):
    === MENU ===
    1. Say Hello
    2. Add Two Numbers
    3. Show Items
    4. Exit

    Select an option: 1
    Hello!

    Select an option: 4
    Exiting...
"""

# TODO:
# 1. Display a menu in a loop.
# 2. Ask the user for a selection.
# 3. Handle valid and invalid selections.
# 4. Implement at least three actions.
# 5. Exit when selected.

def show_menu():
    print("\n=== MENU ===")
    print("1. Say Hello")
    print("2. Add Two Numbers")
    print("3. Show Items")
    print("4. Exit")


def say_hello():
    print("Hello!")


def add_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Result: {a + b}")
    except ValueError:
        print("Invalid input. Please enter numbers.")


def show_items():
    items = ["Apple", "Banana", "Orange"]
    print("Items:")
    for item in items:
        print(f"- {item}")


def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            say_hello()
        elif choice == "2":
            add_numbers()
        elif choice == "3":
            show_items()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()