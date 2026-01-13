
"""
CH01 - Two Sum

Description:
    Given a list of numbers and a target value, determine whether
    two numbers in the list add up to the target. If they do,
    print the two numbers or their indices (your choice).

Requirements:
    - Create a list of numbers (hard-coded or user input).
    - Define a target value.
    - Check if any two numbers add up to the target.
    - If a valid pair exists, print it.
    - If no pair is found, print a message indicating that.

Notes:
    - The focus is on logic and efficiency.
    - Do NOT use built-in shortcuts like combinations from itertools.
    - Use loops to explore possible pairs.

Example:
    Numbers: [2, 7, 11, 15]
    Target: 9

    Output:
    2 + 7 = 9
"""

# TODO:
# 1. Create a list of numbers and a target value.
# 2. Use loops to check all possible pairs.
# 3. If two numbers add up to the target, print them.
# 4. If no pair exists, print a suitable message.

numbers = [5, 2, 4, 9, 1, 3]
target = 6

found = False   
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):   
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")
            found = True

if not found:
    print("No pair exists that adds up to the target.")



