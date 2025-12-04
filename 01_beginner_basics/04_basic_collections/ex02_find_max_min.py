
"""
Ex02 - Find Maximum and Minimum

Description:
    Write a program that asks the user to enter several numbers
    separated by spaces, stores them in a list, and then prints
    the largest number and the smallest number.

Requirements:
    - Ask the user for input (numbers separated by spaces).
    - Split the input into a list of strings.
    - Convert each item to a number (int or float).
    - Find the maximum value.
    - Find the minimum value.
    - Print both values.

Example:
    Enter numbers separated by spaces:
    3 9 1 6

    Maximum: 9
    Minimum: 1
"""

# TODO:
# 1. Ask the user for numbers separated by spaces.
# 2. Split the input into a list.
# 3. Convert each element to a number.
# 4. Find the maximum and minimum values.
# 5. Print both results.

numbers = input("Enter numbers separated by spaces: ")

numbers = numbers.split()

int_numbers = [int(i) for i in numbers]

max_num = max(int_numbers)

print(max_num)

min_num = min((int_numbers))

print(min_num)
