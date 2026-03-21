
"""
Project 03 - Student Grades Manager

Description:
    Create a console application to manage students and their grades.
    The program should allow adding students, assigning grades,
    and viewing basic statistics.

Requirements:
    - Store students and their grades in a suitable data structure
      (for example, a dictionary: { "Alice": [8.5, 9.0], ... }).
    - Provide a menu with options such as:
        1. Add a student
        2. Add a grade to a student
        3. List all students and their grades
        4. Show average grade for a student
        5. Exit
    - Handle cases where:
        - A student does not exist.
        - A student has no grades yet.

Notes:
    - All data can be stored in memory (no files required).
    - The focus is on collections, loops, and basic calculations.

Example (expected behavior):
    === GRADES MANAGER ===
    1. Add student
    2. Add grade
    3. List students
    4. Show student average
    5. Exit

    Select an option: 1
    Enter student name: Alice

    Select an option: 2
    Enter student name: Alice
    Enter grade: 9.0
"""

# TODO:
# 1. Choose a data structure to store students and grades.
# 2. Display a menu in a loop.
# 3. Implement options to add students, add grades, and list data.
# 4. Implement an option to calculate and show a student's average grade.
# 5. Handle invalid inputs and missing students.


def show_menu():
    print("\n=== GRADES MANAGER ===")
    print("1. Add student")
    print("2. Add grade")
    print("3. List students")
    print("4. Show student average")
    print("5. Exit")


def add_student(students):
    name = input("Enter student name: ").strip()

    if name in students:
        print("Student already exists.")
    else:
        students[name] = []
        print(f"Student '{name}' added.")


def add_grade(students):
    name = input("Enter student name: ").strip()

    if name not in students:
        print("Student does not exist.")
        return

    try:
        grade = float(input("Enter grade: "))
        students[name].append(grade)
        print("Grade added.")
    except ValueError:
        print("Invalid grade. Please enter a number.")


def list_students(students):
    if not students:
        print("No students found.")
        return

    for name, grades in students.items():
        print(f"{name}: {grades if grades else 'No grades'}")


def show_average(students):
    name = input("Enter student name: ").strip()

    if name not in students:
        print("Student does not exist.")
        return

    grades = students[name]

    if not grades:
        print("This student has no grades yet.")
        return

    avg = sum(grades) / len(grades)
    print(f"Average grade for {name}: {avg:.2f}")


def main():
    students = {}  # {"Alice": [8.5, 9.0]}

    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            add_student(students)
        elif option == "2":
            add_grade(students)
        elif option == "3":
            list_students(students)
        elif option == "4":
            show_average(students)
        elif option == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()