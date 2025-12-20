
"""
Ex01 - Count Lines in a File

Description:
    Write a program that asks the user for a file name,
    opens the file, counts how many lines it contains,
    and prints the total line count.

Requirements:
    - Ask the user for a file name (e.g., "data.txt").
    - Open the file in read mode.
    - Use a loop to count the lines.
    - Print the total number of lines.

Notes:
    - Assume the file exists for this exercise.
    - No need to handle errors or missing files yet.

Example:
    Enter file name:
    sample.txt

    Total lines: 42
"""

# TODO:
# 1. Ask the user for a file name.
# 2. Open the file in read mode.
# 3. Loop through the file and count the lines.
# 4. Print the total count.

name_file = input("Enter file name: ")

with open ("02_intermediate_core/04_files_and_loops/data/" + name_file , "r") as file:
    counts = 0
    for line in file:
        counts += 1
print(counts)
