"""
Day 151: Bank Account Class

Question:
Create a BankAccount class with deposit, withdraw and balance checks.
"""

# Solution
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amt

acc = BankAccount("Riya", 1000)
acc.deposit(500)
acc.withdraw(2000)
acc.withdraw(300)
print(acc.balance)
