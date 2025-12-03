
"""
Ex01 - List Sum and Average

Description:
    Write a program that asks the user to enter several numbers
    separated by spaces, stores them in a list, and then prints
    both the total sum and the average of those numbers.

Requirements:
    - Ask the user for input (numbers separated by spaces).
    - Split the input into a list of strings.
    - Convert each item to a number (int or float).
    - Calculate the total sum.
    - Calculate the average.
    - Print both values.

Example:
    Enter numbers separated by spaces:
    5 10 15

    Sum: 30
    Average: 10.0
"""

# TODO:
# 1. Ask the user for numbers separated by spaces.
# 2. Split the input into a list.
# 3. Convert each element to a number.
# 4. Calculate the sum and the average.
# 5. Print the results.

numbers = str(input("Enter numbers separated by spaces:"))
list_num = []
list_num = numbers.split()

int_list_num = [int(i) for i in list_num]

total_sum =  sum(int_list_num)
    
print(total_sum)

the_average = total_sum / len(int_list_num)

print(the_average)
