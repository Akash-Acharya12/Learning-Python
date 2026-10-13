#Getters and setters
'''
1. Getters and Setters
Definition: Getters and setters are methods that allow controlled access to an object's attributes.
Purpose: They help in validating data, protecting data from accidental modification, and providing controlled access.
'''
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):     # getter
        return self.__name

    def set_name(self,name):
        self.__name=name
    def get_age(self):
        return self.__age

    def set_age(self,age):
        if isinstance(age,int):
            self.age=age
        else:
            print("You need to insert integer but you gave wrong data type . Try again")
s=Student("Akash",19)
print(s.get_name())
s.set_name("Dakshin")
print(s.get_name())
s.set_age(19)
print(s.get_age())


#Method overloading
'''3. Method Overriding
Definition: Method overriding allows a child class to provide a specific implementation for a method that is already defined in its parent class.
Purpose: It enables a child class to alter or extend the behavior of a parent class method.
'''
class Calculator:
    def add(self,a,b,c=0):#in python for verloading we can use one convension called defalut argument 
        print(a+b+c)
a=Calculator()
a.add(1,2)
a.add(1,2,3)


#Merhod overriding + Super class
'''4. super() Function
Definition: The super() function is used in child classes to call a method from the parent class, enabling access to inherited methods or attributes.
Purpose: It ensures that the parent class's method is executed alongside any additional functionality added in the child class, useful when overriding methods but still needing to incorporate the parent’s behavior.
'''
class Animal:

    def makesound(self):
        print("Animal is making sound")
class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def makesound(self):
        super().makesound()
        print(f"{self.name} is barking")
        print("\n**\n")
    def angry(self):
        super().makesound()
        self.makesound()
        
    
d=Dog("Tommy")
d.makesound()
d.angry()

# another example for super
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} makes sound")
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        super().sound()
        print(f"{self.name} barks")
dog=Dog("Tiga","Jaati nayi")
print("\nSuper\n")
dog.sound()

class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if isinstance(age,int):
            self.__age=age
        else:
            print("Age should be an integer")
s1=Student("Akash",19)
print(s1.get_name())
s1.set_age(25)
print(s1.get_age())

#Abstract class
from abc import ABC, abstractmethod
class vehicle:
    @abstractmethod
    def start_engine(self):
        pass
class Bike(vehicle):
    def __init__(self,name):
        self.name=name
    def start_engine(self):
        print("Starting engine")

b=Bike("Kawasaki ninja")
print(b.name)
b.start_engine()


#problems 
'''
Getters and Setters:

Create a class BankAccount with a private attribute balance.
Write a getter method to retrieve the balance and a setter method to update it, ensuring the balance never goes below zero.
'''
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposite(self,amount):
        self.__balance +=amount
        print(f"{amount} deposited succesfully")
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
            print(f"Withdrawal {amount} sucesseful")
        else:
            print("Insufficient balance")

acc=BankAccount(15000)
print(acc.get_balance())
acc.withdraw(5000)
print(acc.get_balance())
acc.deposite(4000)
print(acc.get_balance())

'''
2.Method Overloading:

Write a class Calculator with a method multiply(). Allow it to take either two or three arguments to multiply two or three numbers.
'''
class Calculator:
    def mul(self,a,b,c=1):
        return a*b*c
math=Calculator()
print("\nResult\n")
print(math.mul(2,5))
print(math.mul(6,4,8))
print("Results")

'''3.Method Overriding:

Create a parent class Shape with a method draw() that prints "Drawing shape".
Create a child class Circle that overrides draw() to print "Drawing circle".
'''
class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")
shape=Circle()
shape.draw()


'''4.Abstract Classes:

Define an abstract class Employee with an abstract method calculate_salary().
Create a subclass Manager that implements calculate_salary() based on working hours and rate per hour.
'''
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Employee):
    def __init__(self,hour,rate):
        self.hour=hour
        self.rate=rate
    def calculate_salary(self):
        return self.hour*self.rate
manger=Manager(40,500)
print(manger.calculate_salary())
