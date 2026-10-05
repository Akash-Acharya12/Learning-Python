#simple car detailes and creating differnt car objects
class car:
    #Attributes
    def __init__(self,brand,model):
        self.brand=brand#instance variable
        self.model=model#instance variable

    def display_info(self):#method
        print(f"{self.brand}{self.model} is my favorite car")

my_car=car("BMW"," M5 Compition")#Object
my_car.display_info()

#Program to create a different objects of person name and their age 
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old")
person1=person("Akash",19)
person2=person("yashas",18)

person1.greet()
person2.greet()


#main class is Dog,  name and breed are attributes and bark is method dog1 and dog2 are objects
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"{self.name} is barking")
dog1=Dog("Rex", "Golden Retriever")
dog2=Dog("tommy", "jarman shefard")
dog1.bark()
dog2.bark()

#mobile price and brand
class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def details(self):
        print(f"This is {self.brand} and it costs {self.price}")
mobile1=mobile("Aplle 17pro max",180000)
mobile2=mobile("Samsung s4",85000)
mobile1.details()
mobile2.details()


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(f"{self.name} scored {self.marks}")
s1=Student("Dakshin",98)
s2=Student("Niketan",70)
s1.display_info()
s2.display_info()

