
"""
Ex03 - Simple Calculator

Description:
    Write a program that asks the user for two numbers
    and an operation (+, -, *, /), then prints the result
    of applying that operation.

Requirements:
    - Ask the user for the first number.
    - Ask the user for the second number.
    - Ask the user for the operation as text: "+", "-", "*", "/".
    - Use if/elif/else to decide which operation to perform.
    - Calculate the result.
    - Print the result in a clear message.
    - (Optional) Handle division by zero.

Example:
    Enter the first number:
    10
    Enter the second number:
    2
    Choose an operation (+, -, *, /):
    /

    The result of 10 / 2 is 5.0
"""

# TODO:
# 1. Ask the user for two numbers and one operation.
# 2. Convert the numbers to int or float.
# 3. Use if/elif/else to perform the chosen operation.
# 4. Print the result.
# 5. (Optional) Handle division by zero if the operation is "/".

"""
Ex03 - Simple Calculator

Description:
    Write a program that asks the user for two numbers
    and an operation (+, -, *, /), then prints the result
    of applying that operation.
"""

 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


symbol1 = input("Choose an operation (+, -, *, /): ")


if symbol1 == "+":
    res = num1 + num2
    print(f"The result of {num1} {symbol1} {num2} is {res:.2f}")

elif symbol1 == "-":
    res = num1 - num2
    print(f"The result of {num1} {symbol1} {num2} is {res:.2f}")

elif symbol1 == "*":
    res = num1 * num2
    print(f"The result of {num1} {symbol1} {num2} is {res:.2f}")

elif symbol1 == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        res = num1 / num2
        print(f"The result of {num1} {symbol1} {num2} is {res:.2f}")

else:
    print("ERROR: Invalid operation")
