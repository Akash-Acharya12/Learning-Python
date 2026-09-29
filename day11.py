a,b=22,67
print(f"a:{a} b:{b}")
print("after swap")
a,b=b,a
print(f"a:{a} b:{b}")
c=0
c=a
a=b
b=c
print(f"a:{a} b:{b}")

'''
name=input("Name:")
age=int(input("age:"))
print(name + " you are " + str(age) + "years old")
'''
'''
n=input("Enter a string:")
print(len(n.replace(" ","")))
'''
print("hello\n\tworld\nThis is a backslash:\\")

list=["akak",18 ,"skk",True]
list.remove(list[1])
print(list)
l=[27, 33 ,76 ,12,78]
print(l)
#l.sort(reverse=True)
l.sort()
#l.reverse()
print(l[::-1])
print(l)

d={
"f1":{
"name":"yashwin",
"fav_food":"Biriyani",
"fav_sub":"Kannada"
},
"f2":{
"name":"Dakshin",
"fav_food":"Chicken Tawa",
"fav_sub":"Maths"
}
}
print(d["f1"]["fav_food"])


import time
i=10
while i<0:
    print("count down",i)
    i-=1
    time.sleep(1)
print("Happy newa year")

'''
vowels="aeiou"
count=0
s=input("Enter a strings:")
for letter in s:
    if letter in vowels:
        count+=1
print(count)        
'''
item={
"pencil":5,
"pen":10,
"sheet":20,
"colour":15
}
total=0
for values in item.values():
    total+=values
print(total)
t=0
for key,value in item.items():
    t+=value
print(t)
#print(sum(list(item.values())))

l=[num**2 for num in range(1,11)]
print(l)

list_of_dic=[
{
"name":"Akash",
"marks":18
},
{"name":"Dakshin",
"marks":21
},
{"name":"Niketan",
"marks": 25
}
]
for student in list_of_dic:
    print(f"{student["name"]} --- {student["marks"]}")