
"""
Ex01 - Safe Division

Description:
    Write a program that defines a function to divide two numbers.
    The function should handle division by zero using try/except.
    If division is successful, return the result. If not, print
    an error message.

Requirements:
    - Define a function divide(a, b).
    - Use try/except to catch division by zero.
    - If b is zero, print an error message instead of crashing.
    - In the main part of the script, call the function with
      different values to demonstrate both successful and failed cases.

Notes:
    - No user input required; values can be hard-coded.
    - The focus is on basic exception handling.

Example (expected behavior):
    Result: 5.0
    Error: cannot divide by zero
"""

# TODO:
# 1. Define divide(a, b) with a try/except block.
# 2. Handle division by zero inside the function.
# 3. Demonstrate at least one valid division and one invalid division.


def divide(a, b):
    try:
        result = a / b
        return result
    except Exception as e:
        print(e)


# Successful case
result1 = divide(10, 2)
print("Result:", result1)

# Failed case
result2 = divide(10, 0)
