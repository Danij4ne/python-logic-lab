
"""
Ex02 - Anagram Checker

Description:
    Write a program that asks the user for two words
    and checks whether they are anagrams. Two words are anagrams
    if they contain the same letters in any order.

Requirements:
    - Ask the user for two words.
    - Convert both words to lowercase.
    - Remove spaces (optional, useful for multi-word phrases).
    - Sort the letters of both words or compare letter counts.
    - Print whether the words are anagrams or not.

Notes:
    - Ignore capitalization.
    - Spacing can be ignored to support simple phrases.

Example:
    Enter first word:
    listen
    Enter second word:
    silent

    "listen" and "silent" are anagrams.
"""

# TODO:
# 1. Ask the user for two words.
# 2. Convert them to lowercase and remove spaces if needed.
# 3. Compare the letters of both words.
# 4. Print whether they are anagrams.

word1 = input("Enter first word:")
word2 = input("Enter second word:")

word1 = word1.lower().replace(" " , "")
word2 = word2.lower().replace(" " , "")

wordf1 = "".join(sorted(word1))

wordf2 = "".join(sorted(word2))

if wordf1 == wordf2:
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")

