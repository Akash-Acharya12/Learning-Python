#For loop questions and List comprehinsion
'''
l= [1,2,3,4,5,6,7,8,95]
total=0
for num in l:
    print(total)
    total+=num
print(total)
'''
'''
l= [1,2,3,4,5,6,7,8,95]
dl=[]
for num in l:
    print(dl)
    dl.append(num*2)
   
print(dl)
'''
#Looping through dictionry
'''
student_marks={
"Akash":88,
"Dakshin":98,
"Niketan":89,
"Harsha":77}
for student, marks in student_marks.items():
    print(f"{student}-- {marks}")
'''
students=["Akash","Daskshin","Niketan"]
marks=[23,24,55]
student_marks={}
'''for index, student in enumerate(students):
    student_marks[student]=marks[index]'''
for i in range(len(students)):
    student_marks[students[i]]=marks[i]
print(student_marks)

#list comprehnsion 
l=[x for x in range(1,11)]
dl=[num*2 for num in l]#Multiplying with 2
dl=[num**2 for num in l]#Exponential or sqaring
edl=[num*2 for num in l if num%2==0] #even dubled list 
print(dl)

#List comprehinsion
l=["Akash","Daskshin","Niketan"]
nl=[ch[1] for ch in l ]
print(nl)
#Dictionary comprehinsion
names=["Akash","Daskshin","Niketan"]
d={name:len(name) for name in names }
print(d)

city_pop={
"Bengaluru":84,
"mysuru":11,
"Hubballi":9,
"MAngaluru":5
}
large_cities={city:pop  for city, pop in city_pop.items() if pop>10}
print(large_cities)

#splittng 
s="this is my logic"
str=s.split()
print(str)

'''
x=input("Enter a list of integers:")
h= x.split()
for i in h:
    i=int(i)
    print(i)
'''
'''
#x=input("Enter a list of integers:").split()
'
l=[int(num) for num in input("Enter a list of integers:").split()]
print(l)
'''
cities=["Bemgaluru", "mysore", "Mandya", "Mangalore"]
up_cities=[city.upper() for city in cities]
print(up_cities)
#dictionary comprehnsion problems
nums=[1,2,3,4,5]
squares_dict={num:num**2 for num in nums}
print(squares_dict)

data="apple,banana,orange"
fruits=data.split(",")
print(fruits)