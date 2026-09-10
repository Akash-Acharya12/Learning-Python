#if,else, elif


name= input("Ente your Name only:")
if name=="Akash" or name=="akash":
    print("Hello Akash!")
else:
    print("Who are you!")
    


signal=input("Enter the signal:")
if signal=="Red":
    print("Stop")
elif signal=="Yellow":
    print("Redy")
elif signal =="Green":
    print("Go")
else:
    print("Error!")    



time=float(input("Enter the time;"))
if time>=8 and time<=9:
    print("Its time for Breakfast")
elif time>=12 and time<=13:
    print("Its time for Lunch!")
elif time>=20 and time<=21:
    print("Its dinner time")
else:
    print("Its not a meal time")
    

#ticket discount system

gender=input("Enter Your Gender:")
age=int(input("Enter your age:"))
if gender =="female" or gender== "Female":
    print("Ticket is free")
else:
    if age<=12:
        print("You get a chiled discount")
    elif age >=;60:
        print("You get seniar citizen discount")
    else:
        print("You have to pay full fare")


age=int(input("Enter your age:"))
if age <18:
    print("You get a student membership")
elif age >=60:
    print("You wil get senior citizen membership")
else:
    print("You will get regular membership")