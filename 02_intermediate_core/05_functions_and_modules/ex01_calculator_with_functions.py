
"""
Ex01 - Calculator Using Functions

Description:
    Write a program that defines four functions:
    add, subtract, multiply, and divide. Then, ask the user
    for two numbers and an operation, call the corresponding
    function, and print the result.

Requirements:
    - Define functions: add(a, b), subtract(a, b), multiply(a, b), divide(a, b).
    - Each function should return the result of the operation.
    - Ask the user for two numbers.
    - Ask the user for an operation (+, -, *, /).
    - Call the correct function based on the operation.
    - Print the final result.
    - (Optional) Handle division by zero inside the divide function.

Example:
    Enter first number:
    8
    Enter second number:
    2
    Enter operation (+, -, *, /):
    *

    Result: 16
"""

# TODO:
# 1. Define the four functions: add, subtract, multiply, divide.
# 2. Ask the user for two numbers and an operation.
# 3. Call the correct function based on the operation.
# 4. Print the result.
# 5. (Optional) Handle division by zero in the divide function.


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = add(n1, n2)
elif operation == "-":
    result = subtract(n1, n2)
elif operation == "*":
    result = multiply(n1, n2)
elif operation == "/":
    result = divide(n1, n2)
else:
    result = "Invalid operation"

print("Result:", result)

