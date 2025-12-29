
"""
Ex02 - Bank Account Class

Description:
    Create a BankAccount class that represents a simple bank account
    with basic deposit and withdrawal operations.

Requirements:
    - Define a class named BankAccount.
    - The class should have:
        - an __init__ method that receives an initial balance (default 0).
        - an attribute to store the balance.
        - a deposit(amount) method that increases the balance.
        - a withdraw(amount) method that decreases the balance
          if there are enough funds.
        - a get_balance() method that returns the current balance.
    - In the main part of the script, create a BankAccount object
      and demonstrate deposits, withdrawals, and balance checks.

Notes:
    - Withdrawals should not allow the balance to go negative.
    - You may print a message if the withdrawal cannot be completed.

Example (expected behavior):
    Balance: 0
    Depositing 100...
    Balance: 100
    Withdrawing 40...
    Balance: 60
"""

# TODO:
# 1. Define the BankAccount class with __init__(self, initial_balance=0).
# 2. Store the balance as an instance attribute.
# 3. Implement deposit(amount) and withdraw(amount) methods.
# 4. Implement get_balance() to return the current balance.
# 5. Create an instance and demonstrate basic operations.

class BankAccount:
    def __init__(self, initial_balance):
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount

    def withdraw(self, amount):
        if self.initial_balance >= amount:
            self.initial_balance -= amount
        else:
            print("There are not enough funds")

    def get_balance(self):
        return self.initial_balance
    
    
account = BankAccount(0)

print("Balance:", account.get_balance())

account.deposit(100)
print("Balance:", account.get_balance())

account.withdraw(40)
print("Balance:", account.get_balance())
 