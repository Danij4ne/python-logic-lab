
"""
Ex03 - Right Triangle of Stars

Description:
    Write a program that asks the user for a number N
    and prints a right triangle made of stars (*) with N rows.
    Use nested loops to generate the shape.

Requirements:
    - Ask the user for a number N.
    - Convert the input to an integer.
    - Use nested loops (or a loop that builds each row).
    - The first row should have 1 star, the second row 2, and so on.
    - The last row should have N stars.

Example:
    Enter size:
    5

    *
    **
    ***
    ****
    *****
"""

# TODO:
# 1. Ask the user for the triangle size (N).
# 2. Convert the input to an integer.
# 3. Use loops to print a triangle where the i-th row has i stars.

the_size = int(input("Enter size : "))

for i in range(1, the_size + 1):
    for j in range(i):
        print("*", end="")
    print()


