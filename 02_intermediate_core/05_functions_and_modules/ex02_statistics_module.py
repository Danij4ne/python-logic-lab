
"""
Ex02 - Simple Statistics Module

Description:
    Write a program that defines a small statistics module
    containing the following functions:
        - calculate_sum(numbers)
        - calculate_average(numbers)
        - calculate_max(numbers)
        - calculate_min(numbers)

    Then, ask the user for a list of numbers, call these functions,
    and print the results.

Requirements:
    - Define four functions, each receiving a list of numbers.
    - Each function should return the corresponding result.
    - Ask the user for numbers separated by spaces.
    - Convert the input into a list of numbers.
    - Call each function and print the outputs.

Notes:
    - No built-in functions like sum(), max(), or min() are required,
      but they may be used if desired.
    - Assume the user enters at least one number.

Example:
    Enter numbers:
    4 8 2 6

    Sum: 20
    Average: 5.0
    Max: 8
    Min: 2
"""

# TODO:
# 1. Define four functions: calculate_sum, calculate_average, calculate_max, calculate_min.
# 2. Ask the user for numbers separated by spaces.
# 3. Convert the input into a list of numbers.
# 4. Call each function and print the results.


def calculate_sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result


def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count


def calculate_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def calculate_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


nums = input("Enter numbers: ")

nums = nums.replace(",", " ")
numbers = [int(number) for number in nums.split()]

total = calculate_sum(numbers)
average = calculate_average(numbers)
maximum = calculate_max(numbers)
minimum = calculate_min(numbers)

print("Sum:", total)
print("Average:", average)
print("Max:", maximum)
print("Min:", minimum)


        
        


