#Simple program to take input name and age from the user and and displaying that the boy loves girl and providig their age difference  

boy_name= input("Enter boy name")
boy_age=int(input("Enter boy age: "))
girl_name= input("Enter girl name")
girl_age = int(input("Enter girl age"))
age_diff = abs(boy_age-girl_age)
print(f"{boy_name } loves {girl_name}  and their age diff is {age_diff}")

 
#practice of input and output 

name=input("Enter Your name: ")
age=int(input("Enter your age: "))
print("hello", name, "! Welcome to Python")
print(f"you are {age} years old." )


#addition of two integers
num1= int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum=num1+num2
print(f"Sum of two numbers is:",sum)

#Substraction of two integers
num1= int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sub=abs(num1-num2)
print(f"Substractiion  of two numbers is:",sub)

#MEADIUM LEVEL

#distance from zero
num= int(input("Enter a number:"))
dis=abs(0-num)
print(f"Distance from zero is : {dis} ")

#temperature diffrence
ptemp=int(input("Enter body temperature: "))
ntemp=37 #normal temperature
temp_diff = abs(ntemp-ptemp)
print(f"\n Difference is  {temp_diff} c")

#total_distance
fsteps=10
bsteps=int(input("Enter the backward steps: "))
final_dis=abs(fsteps-bsteps)
print(f"Distance from start {final_dis}")
