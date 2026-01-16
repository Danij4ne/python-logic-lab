
"""
CH03 - Longest Substring Without Repeating Characters

Description:
    Given a string, find the length of the longest substring
    that contains no repeated characters.

Requirements:
    - Create a string (hard-coded or user input).
    - Examine all possible substrings.
    - Track the longest substring that has no repeated characters.
    - Print the length (and optionally the substring itself).

Notes:
    - This is a common string-based interview problem.
    - Focus on logic rather than built-in shortcuts.
    - You may use loops, sets, or tracking structures.

Example:
    Input:
    "abcabcbb"

    Output:
    Longest length: 3
    (substring: "abc")
"""

# TODO:
# 1. Create a string to analyze.
# 2. Find the longest substring without repeating characters.
# 3. Print the length (and optionally the substring).

words = "abcabcbb"

izq = 0
vistos = set()
max_len = 0

for der in range(len(words)):
    c = words[der]

    while c in vistos:
        vistos.remove(words[izq])
        izq += 1

    vistos.add(c)
    max_len = max(max_len, der - izq + 1)

print(max_len)

