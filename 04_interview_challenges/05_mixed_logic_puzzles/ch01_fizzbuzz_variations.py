
"""
CH01 - FizzBuzz Variations

Description:
    Print numbers from 1 to N. For multiples of 3, print "Fizz"
    instead of the number. For multiples of 5, print "Buzz".
    For multiples of both 3 and 5, print "FizzBuzz".
    Otherwise, print the number itself.

Requirements:
    - Define a value N (hard-coded or user input).
    - Loop from 1 to N.
    - Apply the FizzBuzz rules.
    - Print the result for each number.

Notes:
    - This is a classic logic question often used as a warm-up in interviews.
    - Variations may include changing the rules or output.

Example:
    Input:
    N = 15

    Output:
    1
    2
    Fizz
    4
    Buzz
    ...
    FizzBuzz
"""

# TODO:
# 1. Define N.
# 2. Loop from 1 to N.
# 3. Print "Fizz", "Buzz", "FizzBuzz", or the number.

N = 15

for number in range(1, N + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
