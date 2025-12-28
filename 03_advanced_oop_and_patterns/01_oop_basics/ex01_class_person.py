
"""
Ex01 - Person Class

Description:
    Create a simple Person class that represents a person with a name and an age.

Requirements:
    - Define a class named Person.
    - The class should have:
        - an __init__ method that receives name and age.
        - attributes to store the name and age.
        - a method called introduce() that prints a short introduction
          (for example: "Hi, my name is Alice and I am 30 years old.")
    - In the main part of the script, create at least one Person object
      and call the introduce() method.

Notes:
    - Focus on basic class structure and instance methods.
    - No input from the user is required (you can hard-code example values).

Example (expected behavior):
    Hi, my name is Alice and I am 30 years old.
"""

# TODO:
# 1. Define the Person class with __init__(self, name, age).
# 2. Store name and age as instance attributes.
# 3. Implement an introduce() method that prints a short message.
# 4. Create an instance of Person and call introduce().

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def introduce(self):
        print("Hi, my name is " + self.name + " and I am " + str(self.age) + " years old.")


p1 = Person("Alice", 30)
p1.introduce()

        

