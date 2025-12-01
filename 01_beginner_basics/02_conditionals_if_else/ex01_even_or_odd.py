
"""
Ex01 - Even or Odd

Description:
    Write a program that asks the user for a number
    and prints whether the number is even or odd.

Requirements:
    - Ask the user for a number using input().
    - Convert the input to an integer.
    - Use an if/else statement to check if the number is divisible by 2.
    - Print a message saying whether the number is even or odd.

Example:
    Enter a number:
    7

    7 is odd.
"""

# TODO:
# 1. Ask the user for a number.
# 2. Convert the input to an integer.
# 3. Use if/else to check if the number is even or odd.
# 4. Print the result.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

