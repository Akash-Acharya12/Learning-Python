
#Logical operator practice 
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(num1>10 and num2>10)
print(num1<5 or  num2<5)
print(not(num1 > num2))

#Comparision operator Challeng

age=int(input("Enter your age:"))
if (age>=18):
    print(f"You are adult:")
else:
    print("You are minor")


#Membeship operator exersice

string=input("Enter a string:")
print("a" in string)
print("Python" not in  string)

#bitwise operatore Task

a=int(input("Enter first integer:"))
b=int(input("Enter second integer:"))
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(a>>1)