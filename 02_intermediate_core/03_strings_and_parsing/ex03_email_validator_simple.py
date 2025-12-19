
"""
Ex03 - Simple Email Validator

Description:
    Write a program that asks the user for an email address
    and performs a basic validation to check if it looks valid.

Requirements:
    - Ask the user for an email address.
    - Check that the email contains "@".
    - Check that the email contains "." after the "@".
    - Print whether the email is valid or not.

Notes:
    - This is a simple validation, not a full RFC-compliant check.
    - No need to handle complex cases or advanced formatting rules.

Example:
    Enter email:
    user@example.com

    "user@example.com" is a valid email.
"""

# TODO:
# 1. Ask the user for an email address.
# 2. Check if it contains "@".
# 3. Check if there is a "." after the "@".
# 4. Print whether the email is valid.

the_email = input("Enter email: ")

try:
    at_index = the_email.index("@")
    dot_index = the_email.index(".", at_index)

    print("The email is valid")

except ValueError:
    print("The email is not valid")
