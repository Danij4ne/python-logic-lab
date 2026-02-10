
"""
CH01 - Recursive Factorial

Description:
    Write a function that calculates the factorial of a number using recursion.
    The factorial of a number N is defined as:
        N! = N * (N-1) * (N-2) * ... * 1
    Special case:
        0! = 1

Requirements:
    - Define a function factorial(n).
    - Use recursion (the function should call itself).
    - Handle the base case when n is 0 or 1.
    - In the main part of the script, test the function with a few values.

Notes:
    - No loops allowed; recursion must be used.
    - Assume the input will be a non-negative integer.

Example:
    factorial(5) -> 120
    factorial(0) -> 1
"""

# TODO:
# 1. Define factorial(n) using recursion.
# 2. Handle the base case (n == 0 or n == 1).
# 3. Test the function with sample values.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))