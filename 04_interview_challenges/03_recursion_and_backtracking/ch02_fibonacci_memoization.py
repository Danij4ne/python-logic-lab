
"""
CH02 - Fibonacci with Memoization

Description:
    Write a function that returns the Nth Fibonacci number using recursion
    combined with memoization to improve performance.

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(N) = F(N-1) + F(N-2)

Requirements:
    - Define a recursive function fibonacci(n).
    - Use a dictionary (or similar structure) to store previously computed results.
    - Before computing a value, check if it already exists in the memo.
    - In the main part of the script, test the function with a few values.

Notes:
    - Memoization prevents repeated work and makes the algorithm much faster.
    - Assume n is a non-negative integer.

Example:
    fibonacci(6) -> 8
    fibonacci(10) -> 55
"""

# TODO:
# 1. Create a memo dictionary to store computed values.
# 2. Define fibonacci(n) using recursion.
# 3. Before computing, check if n is in the memo.
# 4. Store new results in the memo before returning them.
# 5. Test the function with sample values.
