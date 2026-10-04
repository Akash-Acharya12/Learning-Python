#Functions Advanced

#Variable length Argument
def add(*numbers):#if we want to take unknown valriavle length numbers we should take *arguments
    print(type(numbers))
    return sum(numbers)
print(add(1,2,3,4,5))

#keyword Arguments
def student_info(**details):#if we want to take keyword arguments we should take **kwarg
    print(details)
    for key,value in details.items():
        print(f"{key}: {value}")
student_info(name="Akash", age=18,course="AI and ML")

#Lambda Function /anonimus function
add = lambda x,y ,z:x+y
print(add(1,2,3))

double= lambda x: x*2
print(double(50))

students=[
{"name":"Yashwin", "marks":80},
{"name":"Akash","marks":75},
{"name":"Dakshin","marks":100}
]
students.sort(key=lambda x: x["marks"], reverse=True)
print(students)

#Recursion  (Which calls function itself)
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))


#Nested Functions
def calculate(a,b):
       def add():
            print(a+b)
       def sub():
            print(a-b)
       def mul():
            print(a*b)
       add()
       sub()
       mul()
calculate(4,5)

#Keyword argument
def info(name,age):
    print(f"{name} you are {age} years old")
info("Akash",18)

#Variable length arguments
def total_sum(*numbers):
    result=0
    for num in numbers:
        result+=num
    return result
print(total_sum(1,2,3,4))

#Keyword length arguments
def s_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
s_info(name="Akash",age=18,course="AI and ML")

#lambda function 
square= lambda x:x**2
print(square(5))

#Nested function
def outer(name):
    def inner():
        print(f"Hello! {name} welcome to python")
    inner()
outer("Akash")


#problems
multiply= lambda x,y:x*y
print(multiply(3,4))


def sum_of_n(n):
    if n==0:
        return 0
    else:
        return n +sum_of_n(n-1)
print(sum_of_n(5))


def average(*numbers):
    if numbers==0:
        return 0
    return sum(numbers)/tuple(len(numbers))
print(average(10))