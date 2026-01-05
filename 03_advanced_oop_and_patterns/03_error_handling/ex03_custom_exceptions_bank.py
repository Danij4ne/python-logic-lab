
"""
Ex03 - Custom Exceptions: Bank Withdrawal

Description:
    Create a simple banking system where attempting to withdraw more
    money than the current balance raises a custom exception.

Requirements:
    - Define a custom exception class named InsufficientFundsError.
    - Create a BankAccount class with:
        - an __init__(self, balance) method
        - a withdraw(amount) method
    - Inside withdraw(amount):
        - If amount is greater than balance, raise InsufficientFundsError
        - Otherwise, subtract the amount from the balance
    - In the main part of the script:
        - Create a BankAccount
        - Attempt a valid withdrawal
        - Attempt an invalid withdrawal and handle the exception using try/except

Notes:
    - The focus is on raising and handling custom exceptions.
    - No user input is required; values can be hard-coded.

Example (expected behavior):
    Withdrawal successful. New balance: 60
    Error: insufficient funds
"""

# TODO:
# 1. Define the custom exception InsufficientFundsError.
# 2. Create the BankAccount class with a withdraw(amount) method.
# 3. Raise the custom exception if amount > balance.
# 4. Use try/except to handle the exception when testing the withdrawal.

 
class InsufficientFundsError(Exception):
    pass

 
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")


account = BankAccount(100)

try:
    account.withdraw(40)  
    account.withdraw(80)    

except InsufficientFundsError as e:
    print("Error:", e)


