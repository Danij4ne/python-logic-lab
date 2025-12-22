
"""
Ex03 - Simple Log Analyzer

Description:
    Write a program that asks the user for a log file name
    and analyzes it by counting how many lines contain the word "ERROR".
    Then, print the total number of error lines.

Requirements:
    - Ask the user for a file name (e.g., "log.txt").
    - Open the file in read mode.
    - Loop through each line of the file.
    - Check if the line contains the word "ERROR".
    - Count how many lines match.
    - Print the final count.

Notes:
    - The search can be case-sensitive or case-insensitive.
    - No need to extract timestamps or additional details.

Example:
    Enter log file name:
    system.log

    ERROR lines found: 5
"""

# TODO:
# 1. Ask the user for a log file name.
# 2. Open the file in read mode.
# 3. Loop through each line and check for "ERROR".
# 4. Count how many lines contain the word.
# 5. Print the result.

name_file =  input("Enter log file name: ")

count_lines = 0

with open ("02_intermediate_core/04_files_and_loops/data/" + name_file , "r") as f:
    for line in f: 
        if line.count("ERROR"):
            count_lines += 1

print(f"ERROR lines found: {count_lines}")