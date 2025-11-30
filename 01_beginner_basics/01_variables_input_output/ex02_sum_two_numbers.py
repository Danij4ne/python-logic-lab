
"""
Ex02 - Sum Two Numbers

Description:
    Write a program that asks the user for two numbers
    and prints the sum of those numbers.

Requirements:
    - Ask the user for the first number using input().
    - Ask the user for the second number using input().
    - Convert both inputs to numbers (int or float).
    - Calculate the sum.
    - Print the result in a clear message.

Example:
    Enter the first number:
    5
    Enter the second number:
    7

    The sum of 5 and 7 is 12.
"""

# TODO:
# 1. Ask the user for two numbers using input().
# 2. Convert the inputs to numbers (int or float).
# 3. Add the two numbers.
# 4. Print the result.


first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))

result = first_num + second_num

print(f"The sum of {first_num} and {second_num} is {result}.")


