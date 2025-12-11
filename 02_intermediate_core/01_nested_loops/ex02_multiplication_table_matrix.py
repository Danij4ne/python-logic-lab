
"""
Ex02 - Multiplication Table Matrix

Description:
    Write a program that asks the user for a number N
    and prints an N x N multiplication table using nested loops.

Requirements:
    - Ask the user for a number N.
    - Convert the input to an integer.
    - Use nested loops to generate the table.
    - Each cell should contain (row_index * column_index).
    - Print the table in a clear grid-like format.

Example:
    Enter size:
    3

    1  2  3
    2  4  6
    3  6  9
"""

# TODO:
# 1. Ask the user for the table size (N).
# 2. Convert the input to an integer.
# 3. Use nested loops to generate the multiplication table.
# 4. Print each row on a separate line.

the_size = int(input(" Enter size: "))

for i in range (1,the_size +1 , 1):
    for j in range (1,the_size +1 , 1):
        res = i * j
        print(res , end="")
    print()
    
