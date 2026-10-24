#OOP Challenges
'''
Banking System Simulation
Design a system to simulate a bank's operations, where users can create accounts, deposit and withdraw money, and check their account balance.

Extend functionality to include multiple account types (e.g., savings, current) with unique behaviors like interest calculation or overdraft limits.
Emphasize encapsulation, inheritance and polymorphism.
'''
class Account:
    def __init__(self,id,name,balance):
        self.id=id
        self.name=name
        self._balance=0
    def check_balance(self):
        print(f"Balance:{self._balance}")
    def deposite(self,amount):
        self._balance+=amount
        print(f"Deposite succesful. Updated balance is {self._balance}")
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f"Withdraw succesful. Updated balance is {self._balance}")
        else:
            print("INsuffisient Amount")
class SavingsAccount(Account):
    pass
class CurrentAccount(Account):
    pass
class Bank:
    pass
    