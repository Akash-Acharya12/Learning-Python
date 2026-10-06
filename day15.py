#constructor
class Human:
    
    def __init__(self,name,age):
        print(name)
        self.name=name
        self.age=age
    def walk(self):
        print(f"{self.name} is walking")

a=Human("Akash",19)
l=Human("Likhith",19)
print(a.name)
print(l.age)
a.walk()
l.walk()

class Human:
    
    def __init__(self,name="UNknown",age=0,salary=-1):#Optional Parameters
                                                                                        
        self.name=name
        self.age=age
        self.salary=salary
    def walk(self):
        print(f"{self.name} is walking")

a=Human("Akash",19)
l=Human("Likhith",19,44000)
print(a.name)
print(l.age)
print(l.salary)
a.walk()
l.walk()
paapu=Human()
paapu.name="Suheeb"
paapu.walk()

class Person:
    def __init__(self,name,age,gender):
        self.name=name   #instance variables
        self.age=age
        self.gender=gender
    def identity(self):
        print(f"My self {self.name} and i am {self.age}years old ")
person1=Person("Akash",18,"Male")
person1.identity()

class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def show_info(self):
        print(f"Laptop Brand: {self.brand}, Price: ₹{self.price}")

lap1=Laptop("Asus V16",15000)
lap1.show_info()
lap2=Laptop("Lenovo LOQ",93000)
lap2.show_info()

class Scholarship:
    def __init__(self,name,age,cast,income,gender="Unknown"):
        self.name=name
        self.age=age
        self.gender=gender
        self.cast=cast
        self.income=income
    def selected(self):
        if self.income >80000:
            print(f"{self.name} You are not selected")
        else:
            print(f"{self.name} Congrats You got selected")
student1=Scholarship("Akash",19,"OBC",60000,"male")
student1.selected()
student2=Scholarship("Dakshin",19,"OBC",600000,"male")
student2.selected()

'''Create a Class with a Constructor:

Write a class Movie with attributes title and rating using the __init__() constructor.
Define a method to display the movie’s title and rating.
'''

class Movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    def Ratings(self):
        print(f"{self.title} got {self.rating} IMDB Ratings ")
movie1=Movie("Toxic",7.5)
movie2=Movie("KGF",9.9)
movie1.Ratings()
movie2.Ratings()

'''
Add Default Parameters:

Create a class Employee with attributes name, designation, and salary (default value of salary is 30,000).
Write a method that displays the details of each employee.
Create multiple Employee objects with different values for name and designation, and test the default salary behavior.
'''

class Employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary
    def info(self):
        print(f"{self.name} is working as {self.designation} and his salary is {self.salary}")

emply1=Employee("Akash","Junior Engineer",200000)
emply2=Employee("Niketan","Junior engineer")
emply1.info()
emply2.info()