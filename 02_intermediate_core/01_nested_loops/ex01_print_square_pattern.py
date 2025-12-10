
"""
Ex01 - Print Square Pattern

Description:
    Write a program that asks the user for a number N
    and prints an N x N square made of a chosen character.
    Use nested loops to generate the pattern.

Requirements:
    - Ask the user for a number N (size of the square).
    - Ask the user for a character or symbol.
    - Use nested loops (a loop inside another loop).
    - Print an N x N square using the chosen character.

Example:
    Enter size:
    4
    Enter character:
    *

    ****
    ****
    ****
    ****
"""

# TODO:
# 1. Ask the user for the square size (N).
# 2. Ask the user for a character.
# 3. Use nested loops to print an N x N square.


the_size = int(input("Enter size:" ))
the_char = input("Enter character:")

for i in range (0,the_size , 1):
    for j in range (0,the_size , 1):
        print(the_char, end="")
    print()


