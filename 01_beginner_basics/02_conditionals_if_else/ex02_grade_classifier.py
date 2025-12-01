

"""
Ex02 - Grade Classifier

Description:
    Write a program that asks the user for a score between 0 and 100
    and prints a grade category based on the value.

Example Rules:
    90 - 100  -> "Excellent"
    70 - 89   -> "Good"
    50 - 69   -> "Pass"
    0 - 49    -> "Fail"

Requirements:
    - Ask the user for a score using input().
    - Convert the input to an integer.
    - Use if/elif/else to classify the score.
    - Print the corresponding category.

Example:
    Enter your score:
    85

    Your grade is: Good
"""

# TODO:
# 1. Ask the user for a score (0-100).
# 2. Convert the input to an integer.
# 3. Use if/elif/else to classify the score.
# 4. Print the grade category.

number = int(input("Enter your score : "))

if number > 100 or number < 0:
    print("ERROR NUMBER, try again")

elif number >= 90:
    print("Excellent")
elif number >= 70:
    print("Good")
elif number >= 50:
    print("Pass")
else:
    print("Fail")



