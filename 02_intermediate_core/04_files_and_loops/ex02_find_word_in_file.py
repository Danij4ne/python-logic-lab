
"""
Ex02 - Find a Word in a File

Description:
    Write a program that asks the user for a file name
    and a word to search for. The program should open the file,
    count how many times the word appears, and print the result.

Requirements:
    - Ask the user for a file name.
    - Ask the user for a word to search for.
    - Open the file in read mode.
    - Loop through the file line by line.
    - Count how many times the word appears.
    - Print the total occurrences.

Notes:
    - The search can be case-sensitive.
    - A simple string search is enough for this exercise.

Example:
    Enter file name:
    sample.txt
    Enter word to search:
    python

    "python" found 3 times.
"""

# TODO:
# 1. Ask the user for a file name and a search word.
# 2. Open the file in read mode.
# 3. Loop through each line and count occurrences of the word.
# 4. Print the total count.

file_name = input("Enter file name: ")

word_name  = input("Enter word to search:")

with open ("02_intermediate_core/04_files_and_loops/data/" + file_name , "r") as f:
    word_counts = 0 
    for lines in f:
        word_counts += lines.count(word_name)

print(f"{word_name} found {word_counts} times ")