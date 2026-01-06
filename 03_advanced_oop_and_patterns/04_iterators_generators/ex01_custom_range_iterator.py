

"""
Ex01 - Custom Range Iterator

Description:
    Create a custom iterator that behaves like the built-in range(),
    generating numbers from a start value up to (but not including) an end value.

Requirements:
    - Define a class named CustomRange.
    - The class should:
        - take start and end values in the constructor (__init__)
        - implement __iter__() and __next__() methods
    - __next__() should return the next number in the sequence,
      and stop when the end is reached by raising StopIteration.
    - In the main part of the script, iterate over CustomRange using a for loop
      and print each value.

Notes:
    - No user input is required; values can be hard-coded.
    - Focus on how iterators work internally.

Example (expected behavior):
    5
    6
    7
    8
    9
"""

# TODO:
# 1. Define the CustomRange class with start and end.
# 2. Implement __iter__() to return self.
# 3. Implement __next__() to return the next value or raise StopIteration.
# 4. Create an instance and loop through it, printing each value.


class CustomRange:
    def __init__(self, start, end):
        self.start = start    
        self.end = end        

    def __iter__(self):
        return self         

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        valor = self.start
        self.start += 1
        return valor

for x in CustomRange(5, 10):
    print(x)
    
