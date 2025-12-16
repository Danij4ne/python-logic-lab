
"""
Ex03 - Invert a Dictionary

Description:
    Write a program that starts with a dictionary where each key
    is associated with a value, and creates a new dictionary where
    the original values become keys and the original keys become values.

Requirements:
    - Create a sample dictionary in the code (for example: {"a": 1, "b": 2, "c": 3}).
    - Invert the dictionary so that it becomes {1: "a", 2: "b", 3: "c"}.
    - Print the original dictionary and the inverted dictionary.

Notes:
    - Assume that all values in the original dictionary are unique.
    - No user input is required for this exercise.

Example:
    Original: {"x": 10, "y": 20, "z": 30}
    Inverted: {10: "x", 20: "y", 30: "z"}
"""

# TODO:
# 1. Create a sample dictionary.
# 2. Invert it by swapping keys and values.
# 3. Print both the original and the inverted dictionary.

original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {}

for key, value in original_dict.items():
    inverted_dict[value] = key

print("Original:", original_dict)
print("Inverted:", inverted_dict)

