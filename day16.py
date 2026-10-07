#Abstraction
'''
Definition: Abstraction hides the complex inner workings of an object, exposing only the essential parts for interaction.
Real-World Example: Think about driving a car. You use the steering wheel and pedals to control the car, without needing to know the engine mechanics or braking systems.
'''
class Car:
    def start_engine(self):
        print("Car is starting")
    def accelarate(self):
        print("Car is accelarating")
    def stop(self):
        print("Car is stopping")
car=Car()
car.start_engine()# Abstracts complex internal workings
car.accelarate()
car.stop()      


#Encapsulation
'''
Definition: Encapsulation involves wrapping data and methods that operate on that data within one unit, such as a class. This protects the data from external interference and misuse, improving security and maintainability.
Real-World Example: Imagine an ATM machine—you interact with a limited interface (e.g., withdraw, deposit, check balance) but do not have access to the inner mechanics or backend functions.
'''

class ATM:
    def __init__(self,balance):
        self.__balance=balance # here __balance is private attribute
    def deposite(self,amount):
        self.__balance+=amount
        print(f"Deposited {amount} . Current Balance {self.__balance}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"withdraw {amount}. available balance {self.__balance}")
        else:
            print("Insufficent balance")
acc1=ATM(5000)
acc1.withdraw(6000)
acc1.withdraw(4500)
acc1.deposite(2000)
#acc1._ATM__balance()  gives error because of encapsulation


#a User class for storing login information:
class User:
    def __init__(self,username,password):
        self.username=username
        self.__password=password

    def get_username(self):
        return self.username
    def check_password(self,password):
        #print(self.__password)
        return password==self.__password
    
user=User("Admin","Admin@2kl")
print(user.get_username())
print(user.check_password("Akash234"))
print(user.check_password("Admin@2kl"))


#Using a Database class:
class Database:
    def __init__(self):
        self.__storage={}
    def save_data(self,key,value):
        self.__storage[key]=value
        print(f"Data is saved to {key}")
    def get_data(self,key):
        return self.__storage.get(key,"No data available")
db=Database()
db.save_data("user_01",{"name":"Akash","USN":"4SN25AI004"})
print(db.get_data("user_01"))


'''
Create a BankAccount class with private attributes for account_number and balance.
Add methods to check balance, deposit, and withdraw funds.
Try accessing the balance directly and observe the result.
'''
class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance

    def check_balance(self):
        print(f"balance {self.__balance}")

    def deposite(self,amount):
        self.__balance+=amount
        print(f"Deposite {amount} successful")
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance-=amount
            print(f"Withdrawal {amount} succesfull")
        else:
            print("Insuffisint Amount")

acc1=BankAccount(123456789,5000)

acc1.deposite(250)  
acc1.withdraw(650) 
acc1.check_balance()