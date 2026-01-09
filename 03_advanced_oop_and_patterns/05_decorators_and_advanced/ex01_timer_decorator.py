
"""
Ex01 - Timer Decorator

Description:
    Create a decorator that measures how long a function takes to run
    and prints the execution time.

Requirements:
    - Define a decorator named timer.
    - The decorator should:
        - record the start time
        - call the wrapped function
        - record the end time
        - print the elapsed time
    - Apply the decorator to a function of your choice
      (for example, a function that loops many times).
    - Run the decorated function to demonstrate the timing.

Notes:
    - You may use the time module (time.time()).
    - The focus is on understanding how decorators wrap functions.

Example (expected behavior):
    Function took 0.32 seconds to execute
"""

# TODO:
# 1. Define the timer decorator.
# 2. Measure the time before and after calling the function.
# 3. Apply the decorator to a sample function.
# 4. Run the function and print the elapsed time.

import time

def timer(func):
    def wrapper():
        start = time.time()     
        func()                    
        end = time.time()        
        elapsed = end - start    
        print(f"Function took {elapsed:.2f} seconds to execute")
    return wrapper


@timer
def slow_function():
    total = 0
    for i in range(10_000_000):
        total += i

slow_function()

