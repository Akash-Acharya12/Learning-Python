#Inheritance 
'''
Inheritance allows us to inherit the attributes and methods from another class,facilitating reuse
'''
class Family:
    def __init__(self,surname):
        self.surname=surname
class Child(Family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name=name
child=Child("Acharya","Akash")
print(f"{child.name} {child.surname}")


#Login interface using inheritance
print("\nProgram for user login\n")
class User:
    def __init__(self,username):
        self.username=username
    def login(self):
        print(f"{self.username} Logged in")
class Admin(User):
    def del_user(self,user):
        print(f"{self.username} deleted the {user}")
u=User("444")
a=Admin("Akash")
print(a.username)

a.login()
a.del_user(u.username)

class Vehicle:
    def start(self):
        print("Starting..")
class Bike(Vehicle):
    def ride(self):
        print("Ride the bike")
move=Bike()
move.start()
move.ride()

#Polymorphism
'''
Definition: Polymorphism allows objects of different classes to be treated as objects of a common superclass, but they can behave differently depending on the object type.
Real-World Example: Think of animals making sounds—both dogs and cats make sounds, but each produces a distinct sound. They share a common method
'''

class Animal:
    def make_sound(self):
        print("Animal is making sound")
class Dog:
    def make_sound(self):
        print("Dog Barking")
class Cat:
    def make_sound(self):
        print("Cat meowing")
animals=[Dog(),Cat()]
for animal in animals:
    animal.make_sound()


class nortifcation:
    def send(self):
        pass
class EmailNortification(nortifcation):
    def send(self):
        print("Sending Email")
class SMSnortification(nortifcation):
    def send(self):
        print("Sending SMS")
nr=[EmailNortification(),SMSnortification()]
for nortify in nr:
    nortify.send()


class Shape:
    
