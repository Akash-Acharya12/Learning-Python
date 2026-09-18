#While loop 

condition=True
while condition:
    print("Condition is true")



is_failed =True
count=1
while is_failed and count<=100:
    print(f"Try again {count}")
    count+=1
print("I Give Up")


#metod 2 using if and break in while statement

is_failed =True
count=1
while is_failed :
    if count%2!=0:
        count+=1
        continue
    print(f"Attempt  {count}")
    count+=1
    if count>100:
        break
   
print("I Give Up")


i=0
while i<10:
    print(i *"Akash ")
    i+=1

i=0 #1,2,3
while i<10:
    x=0  #1,2,3
    while x<i:   #0<0, 0<1,1<1,1<2,2<2,3<2,3<                    IMPORTANT Trace carefully
        print("Akash", end="-") 
        #print(x)
        x+=1
    print("")
    i+=1


#ATM PIN
pin=1234
trails=1
while trails<=3:
    i_pin=int(input(f"Trail-{trails} | Enter your pin:"))
    if i_pin==pin:
        print("CORRECT!")
        break
    else:
        print("INCORRECT")
        trails+=1 

sheep_count=1
while sheep_count<=10:
    if sheep_count ==4:
        sheep_count+=1
        
    print(f"Sheep count {sheep_count}")
    sheep_count+=1

available_seats=5
while available_seats>0:
    print(f"Available seats={available_seats}")
    booking=input("Do you want to book a seat:(yes/no):").lower()
    if booking == "yes":
        available_seats-=1
        print("Seat booked!")
    else:
        print("Booking canceled")
        break
#print("All seats are BOOKED!")
if available_seats<=0:
   print("All seats are BOOKED!")


snacks_available=3
money=10
while snacks_available >0 and money>0:
    print(f"Snacks available:{snacks_available}")
    buy=input("Do you want to buy snacks for $5:(yes/no)").lower()
    if buy=="yes":
        snacks_available-=1
        money-=5
        print("Snacks Purchased")
    else:
         print("No purchase made")
print("Either snacks not available or you don't have money")


num=1
while num<=20:
    if num%2!=0:
        print(num)
    num+=1

count=10
while count>0:
    print(f"Count Down {count}")
    count-=1
print("Happy New Year!")