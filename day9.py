#For loop

bag=["red", "Yellow", "orange", "blue"]
for ball in bag:
    print(ball)

name="AKASH"
for letter in name:
    print(letter*2)

name = "Akash"
for index, letter in enumerate(name):
    print(letter * (index+1))

nums=[1,23,4,5,6,78]
for nu in nums:
    print(nu,end=" ")

l=[22,33,54,65,78,90]
for index, num in enumerate(l):
    print(f"{num} is in index {index}")

l=[22,33,54,65,78,90]
for index, num in enumerate(l):
    print(num)
    if num==14:
        break
else:
    print("All printed")

d={
"name":"Akash",
"age":18,
"income":0}
for key,value in d.items():
    print(key , " " ,value)

for i in range(2,3):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")

#Finding city and skipping city using continue and break
cities=["Madikeri", "Mangaluru", "Siddapura","Kushalnagara","Bengaluru"]
for city in cities:
        if city=="Kushalnagara":
            #print(f"found {city}!")
            #break
            continue
        print(city)

cities=["Madikeri", "Mangaluru", "Siddapura","Kushalnagara","Bengaluru"]
for index, city in enumerate(cities):
    print(f"city -{index+1}: {city}")