
"""
Ex02 - Unique Elements Using a Set

Description:
    Write a program that asks the user to enter several values
    separated by spaces, stores them in a list, and then uses a set
    to extract only the unique elements. Finally, print the unique values.

Requirements:
    - Ask the user for input (values separated by spaces).
    - Split the input into a list.
    - Convert each value to a number (int or float) if needed.
    - Create a set to remove duplicates.
    - Print the unique elements.

Notes:
    - Sets automatically remove duplicate values.
    - The order of the output does not matter.

Example:
    Enter values:
    1 2 2 3 4 4 4 5

    Unique values: {1, 2, 3, 4, 5}
"""

# TODO:
# 1. Ask the user for values separated by spaces.
# 2. Split the input into a list.
# 3. Convert each value to a number if needed.
# 4. Create a set from the list to remove duplicates.
# 5. Print the unique values.

numbers = input("Enter values: ")
my_set = {int(i) for i in numbers.split()}

print(my_set)


