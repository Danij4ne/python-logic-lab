
"""
CH01 - Binary Search

Description:
    Implement binary search to find a target value inside a sorted list.
    Binary search works by repeatedly dividing the search interval in half.

Requirements:
    - Create a sorted list of numbers.
    - Define a target value to search for.
    - Use binary search (NOT linear search).
    - If the target is found, print its index.
    - If not found, print a message indicating that.

Notes:
    - No built-in search functions.
    - Use a loop or recursion.
    - The list must be sorted for binary search to work.

Example:
    Numbers: [1, 3, 5, 7, 9, 11]
    Target: 7

    Output:
    Found at index 3
"""

# TODO:
# 1. Create a sorted list and a target value.
# 2. Implement binary search logic.
# 3. Print the index if found, or a message if not found.

"""
CH01 - Binary Search
"""

# 1. Create a sorted list and a target value
numbers = [1, 3, 5, 7, 9, 11]
target = 7

# 2. Implement binary search logic
left = 0
right = len(numbers) - 1
found = False

while left <= right:
    mid = (left + right) // 2  # middle index
    
    if numbers[mid] == target:
        print(f"Found at index {mid}")
        found = True
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# 3. Print message if not found
if not found:
    print("Target not found")