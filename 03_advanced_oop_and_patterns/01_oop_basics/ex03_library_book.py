
"""
Ex03 - Library Book Class

Description:
    Create a Book class that represents a library book with a title,
    an author, and a status indicating whether the book is available
    or checked out.

Requirements:
    - Define a class named Book.
    - The class should have:
        - an __init__(self, title, author) method.
        - attributes to store title, author, and availability status
          (default status: available).
        - a checkout() method that marks the book as checked out
          if it is currently available.
        - a return_book() method that marks the book as available again.
        - a display_info() method that prints the book's details and status.
    - In the main part of the script, create a Book object and
      demonstrate checking it out and returning it.

Notes:
    - You may store status as a boolean or a string.
    - Print messages indicating each action.

Example (expected behavior):
    Title: The Hobbit
    Author: J.R.R. Tolkien
    Status: Available

    Checking out the book...
    Status: Checked Out

    Returning the book...
    Status: Available
"""

# TODO:
# 1. Define the Book class with title, author, and status.
# 2. Implement checkout(), return_book(), and display_info().
# 3. Create an instance and demonstrate the full workflow.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def checkout(self):
        if self.status == "Available":
            print("Checking out the book...")
            self.status = "Checked Out"
        else:
            print("The book is already checked out.")

    def return_book(self):
        print("Returning the book...")
        self.status = "Available"

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", self.status)

        
book1 = Book("The Hobbit", "J.R.R. Tolkien")

book1.display_info()
print()

book1.checkout()
book1.display_info()
print()

book1.return_book()
book1.display_info()















