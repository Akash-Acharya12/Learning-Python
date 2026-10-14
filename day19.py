#Problems  
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def details(self):
        print(f"{self.brand}  price is={self.price}")
samsung=Mobile("SamsungS24 Ultra", 60000)
apple=Mobile("Apple",175000)
samsung.details()
apple.details()

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(f"{self.name} scored {self.marks} marks")
s1=Student("Mohit",55)
s2=Student("Raju",85)
s3=Student("Manoj",77)
s1.display_info()
s2.display_info()
s3.display_info()


class Movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    def display_info(self):
        print(f"{self.title} has {self.rating} rating")
m1=Movie("One piece film: Red",7.5)
m2=Movie("One piece film: Stampade",8.2)
m3=Movie("One piece film:God vally",10)
m1.display_info()
m2.display_info()
m3.display_info()

class Employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary
    def display_info(self):
        print(f"{self.name} is working as a {self.designation} and has salary is upto {self.salary}")
e1=Employee("Ramu","Junior Engenior")
e2=Employee("Ramesh","secoretry",35000)
e3=Employee("Abilash","Senior Engineer",85000)
e1.display_info()
e2.display_info()
e3.display_info()

class BankAccount:
    def __init__(self,acc_number,balance):
        self.__acc_number=acc_number
        self.__balance=balance
        
    def check_balance(self):
        return self.__balance
    def deposite(self,amount):
        self.__balance+=amount
        print(f"{amount} Deposited sucessfully")
    def witdraw(self,amount):
        if self.__balance >amount:
            self.__balance-=amount
            print(f"{amount} withdrawal sucessefull")
        else:
            print("Insuffisient Balance")
acc1=BankAccount(45457889,4500,"Akash")
print(acc1.check_balance())
