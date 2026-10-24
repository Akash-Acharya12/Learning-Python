# Simple calculator using functions

'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("Error division by zero is not valid")
    else:
        return a/b
def menu():
    print(" 1.Add\n 2.Substract\n 3.Multiply\n 4.divide\n 5.Quit")
while True:
    menu()
    choice=int(input("Enter your choice(1-5):"))
    if choice in {1,2,3,4}:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        if choice==1:
            print(f"\nResult:{add(a,b)}\n")
        elif choice==2:
            print(f"\nResult:{sub(a,b)}\n")
        elif choice==3:
            print(f"\nResult:{mul(a,b)}\n")
        else: 
            print(f"\nResult:{div(a,b)}\n")
    elif choice==5:
        print("Quitting......")
        break
    else:
        print("Invalid choice try again")
        '''

#Banking System: Write a menu-driven program to simulate a basic banking system with options like:

'''
Check Balance
Deposit Money
Withdraw Money
Exit


def menu():
    print("-----Banking system------")
    print("1.Check balance\n2.Deposite\n3.Withdraw\n4.Quit")
balance=0
while True:
    menu()
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"Balance --{balance}")
    elif choice==2:
        amount=int(input("Enter your amount for deposite:"))
        balance+=amount
        print(f"{amount} deposited successfully")
    elif choice==3:
        amount=int(input("Enter your amount to withdraw:"))

        if balance>amount:
            balance-=amount
            print(f"Withdrawal {amount} succesful")
        else:
            print("Insufficient balance")
    else:
        print("Thank you for usinf our banking System")
        break
'''

'''Grocery Store Menu:

Create a program where users can:
Add items to their cart.
Remove items.
View the total price.
Exit
total=0
def menu():
    print("1.Milk--- 20")
    print("2.Sugar---35")
    print("3.Coffee Powder---2")
    print("4.Rice---60")
    print("5.Tomato---35")
    print("6.potato---25")

def add_items():
    menu()
    global total
    choice=int(input("Enter your choice to add item to cart:"))
    if choice==1:
        total+=20
    elif choice==2:
        total+=35
    elif choice==3:
        total+=2
    elif choice==4:
        total+=60
    elif choice==5:
        total+=35
    elif choice==6:
        total+=25
    else:
        print("Invalid choice")
def remove_items():
    menu()
    global total
    choice=int(input("Enter your choice to add item to cart:"))
    if choice==1:
        total-=20
    elif choice==2:
        total-=35
    elif choice==3:
        total-=2
    elif choice==4:
        total-=60
    elif choice==5:
        total-=35
    elif choice==6:
        total-=25
    else:
        print("Invalid choice")

            
while True:
    print("-----Welcome to our shop-------")
    print("Select the operation")
    print("1.Add items to cart")
    print("2.Remove items from cart")
    print("3.View total price")
    print("4.Exit")
    choice=int(input("Enter your choice for an operation:"))
    if choice==1:
        add_items() 
    elif choice==2:
        remove_items()
    elif choice==3:
        print(f"Total price {total}")
    elif choice==4:
        print("Thank you for visiting our grocery")
        break
    else:
        print("Invaid choice")
'''




'''Educational System:

Write a program with options to:
Add student details.
Display student details.
Exit.
'''
def operations():
    print("----Student details-----")
    print("1.Add student detatils")
    print("2.display student details")
    print("3.Exit")
students=[]
def add_student():
    
    n=int(input("Enter number of students:"))
    for i in range(1,n+1):
        name=input(f"Enter student {i} name:")
        age=int(input("Enter student age:"))
        usn=input("Enter student usn:").upper()
        student={
            "Name":name,
            "age":age,
            "USN":usn
        }
        students.append(student)

while True:
    operations()
    choice=int(input("Enter your choice (1-3):"))
    if choice==1:
        add_student()
    elif choice==2:
        if len(students)==0:
            print("No student records avaiable!")
        else:
            for student in students:
                print(student)
    elif choice==3:
        break
    else:
        print("Invalid choice")

        
        
    


