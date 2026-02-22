
"""
CH02 - Bubble Sort

Description:
    Implement the Bubble Sort algorithm to sort a list of numbers
    in ascending order. Bubble Sort repeatedly compares adjacent
    elements and swaps them if they are in the wrong order.

Requirements:
    - Create an unsorted list of numbers (hard-coded or user input).
    - Implement Bubble Sort using nested loops.
    - Sort the list in ascending order.
    - Print the list before and after sorting.

Notes:
    - Do NOT use built-in sorting functions like sort() or sorted().
    - Bubble Sort is not efficient, but it is a common interview exercise
      for understanding sorting logic.

Example:
    Input:
    [5, 1, 4, 2, 8]

    Output:
    [1, 2, 4, 5, 8]
"""

# TODO:
# 1. Create an unsorted list.
# 2. Use nested loops to compare and swap adjacent elements.
# 3. Continue until the list is fully sorted.
# 4. Print the list before and after sorting.


# 1. Create an unsorted list
numbers = [5, 1, 4, 2, 8]

print("Before sorting:", numbers)

# 2. Bubble Sort using nested loops
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        # 3. Compare adjacent elements
        if numbers[j] > numbers[j + 1]:
            # Swap if they are in the wrong order
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# 4. Print sorted list
print("After sorting:", numbers)