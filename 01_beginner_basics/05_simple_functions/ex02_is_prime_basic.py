
"""
Ex02 - Basic Prime Check

Description:
    Write a function called is_prime that takes a number
    and returns True if the number is prime, and False otherwise.
    Then, ask the user for a number, call the function,
    and print whether the number is prime or not.

Requirements:
    - Define a function named is_prime(n).
    - A prime number is greater than 1 and divisible only by 1 and itself.
    - Use a loop to check divisibility.
    - Return True if prime, False if not.
    - Ask the user for a number and call the function.
    - Print the result in a clear message.

Example:
    Enter a number:
    7

    7 is prime.
"""

# TODO:
# 1. Define a function is_prime(n).
# 2. Use a loop to check if n has any divisors other than 1 and itself.
# 3. Return True if prime, False otherwise.
# 4. Ask the user for a number.
# 5. Call the function and print the result.

def is_prime(num):
    sums = 0
    for i in range(1, num + 1, 1):
        if num % i == 0:
            sums += 1
    
    if sums == 2:
        return ("is Prime")
    else:
        return ("is not Prime")


user_num = int(input("Enter a number:"))

result = is_prime(user_num)

print(f"{user_num} {result} ")

