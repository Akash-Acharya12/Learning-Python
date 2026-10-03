#Functions
def greet():
    print("Hello, Good morning")

greet()

# Simple Marriage details code
def marriage(boy, girl):#parameters
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} married {girl}")
marriage("Akash","XYZ")#positional arguments
marriage("Dakshin","Sneha")
marriage(boy="Yashwin",girl="Unknown")#Keyword arguments

#tables using function
def tables(num):
    for i in range(1,11):
        print(f"{num} X {i}= {num*i}")

tables(4)
tables(5)
tables(6)

def marriage(boy,girl="XYX"):#Default Parameters girl ="XYX"
    print(f"{boy} married {girl}")
marriage("koushik")


#Function using return function 
def func(num):
    return int(str(num)*4)
a=100
#func(2)
b=func(2)
print(a+b)


#global and Local Varible
def any():
    x="Akash" #It is a local variable
    print(x)
    print(y)#you can access y Which is a global variable
#You cant access a local variable which initialised inside the function
Y="Koushik" #it is an global variable