"""
Ex01 - Palindrome Checker

Description:
    Write a program that asks the user for a word or phrase
    and checks whether it is a palindrome. A palindrome reads
    the same forward and backward.

Requirements:
    - Ask the user for a word or phrase.
    - Remove spaces (optional but recommended).
    - Convert the text to lowercase.
    - Check if the text reads the same forwards and backwards.
    - Print whether it is a palindrome or not.

Notes:
    - Ignore capitalization.
    - Spacing can be ignored for a more flexible check.

Example:
    Enter text:
    racecar

    "racecar" is a palindrome.
"""

# TODO:
# 1. Ask the user for a word or phrase.
# 2. Remove spaces and convert to lowercase.
# 3. Check if the text is the same forwards and backwards.
# 4. Print the result.

text = input("Enter text: ")

clean_text = "".join(i.lower() for i in text.split())

palindrome = True
total = len(clean_text)

for i in range(total):
    if clean_text[i] != clean_text[total - 1 - i]:
        palindrome = False
        break




