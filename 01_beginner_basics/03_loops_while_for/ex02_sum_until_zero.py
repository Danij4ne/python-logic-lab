
"""
Ex02 - Sum Until Zero

Description:
    Write a program that repeatedly asks the user for numbers
    and keeps a running total. The program should stop when
    the user enters 0, and then print the total sum.

Requirements:
    - Use a loop (while recommended).
    - Ask the user for a number each time.
    - Add the number to the total.
    - Stop when the user enters 0.
    - Print the final sum.

Example:
    Enter a number:
    5
    Enter a number:
    3
    Enter a number:
    0

    Total sum: 8
"""

# TODO:
# 1. Create a variable to store the running total.
# 2. Use a loop to repeatedly ask the user for numbers.
# 3. Add each number to the total.
# 4. Stop the loop when the user enters 0.
# 5. Print the final total.


myNumber = 0
while True : 
    num = int(input("Enter a number :"))
    if num == 0:
        break;
    myNumber += num
print(f"Total sum: {myNumber}")

