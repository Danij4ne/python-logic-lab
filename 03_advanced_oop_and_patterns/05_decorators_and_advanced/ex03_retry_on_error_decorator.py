
"""
Ex03 - Retry on Error Decorator

Description:
    Create a decorator that retries calling a function if it raises an exception.
    The function should be attempted multiple times before finally failing.

Requirements:
    - Define a decorator named retry.
    - The decorator should:
        - accept a parameter specifying the number of retry attempts
        - call the wrapped function
        - if the function raises an exception, try again
        - after all attempts fail, print an error message or re-raise the exception
    - Apply the decorator to a function that sometimes raises an exception
      (for example, dividing by a random number that could be zero).
    - Run the decorated function to demonstrate the retry behavior.

Notes:
    - You may import the random module for testing purposes.
    - The focus is on understanding decorators with arguments
      and handling exceptions during retries.

Example (expected behavior):
    Attempt 1 failed...
    Attempt 2 failed...
    Attempt 3 failed...
    All attempts failed.
"""

# TODO:
# 1. Define the retry decorator that accepts a number of attempts.
# 2. Retry calling the function if it raises an exception.
# 3. Apply the decorator to a sample function that may fail.
# 4. Demonstrate the retry behavior.


import random

def retry(attempts: int = 3):
    def decorator(func):
        def wrapped(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed... ({e})")
                    if attempt == attempts:
                        print("All attempts failed.")
                        raise   
        return wrapped
    return decorator


def divide_random():
    n = random.randint(0, 2)   
    print("Random number:", n)
    return 10 / n

 
divide_random()





