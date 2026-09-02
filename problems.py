#Daily Problems
#1st
marks=[10,4,7,10,8,8,3]
nl=[]
for mark in marks:
    nl.append(mark)
    if mark in nl:
        mark+=1
print(nl)

#2nd 
# list basics Sum of elements
nums=[2,5,7,3]
total=0
for num in nums:
    total+=num
print(total)

#List basics-Largest elements
l=[12,5,19,7,3]
'''
yl.sort()
print(l[-1])
'''
lg=l[0]
for num in l:
    if num>lg:
        lg=num
print(lg)

# Remove Duplicates
nums=[3,1,3,2,1,4]
nl=[]
for num in nums:
    if num in nl:
        continue
    nl.append(num)
print(nl)       
print("********")
# Another  Easy code for this
nums=[3,1,3,2,1,4]
result=[]
for num in nums:
    if num not in result:
        result.append(num)
print(result) 


# List count even and odd
n=[1,4,7,10,12,15]
even_count=0
odd_count=0
for num in n:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)

# Reverse a list Manually without revese()
l=[1,2,3,4,5]
print(l[::-1])
#Another approach
result=[]
for n in l[::-1]:
    result.append(n)
print(result)

#Access and Unpack
point=(10,20)
x=point[0]
y=point[1]
print(f"x={x}, y={y}")
#Another approach
point=(10,20)
a,b=point
print(f"x={a},y={b}")

#Tuple -count and index
data=(4,2,4,7,4,9)
count=0
for d in data:
    if d ==4:
        count+=1
print(f"4 occurs {count} times, first index {data.index(4)}")
#Another approach 
data=(4,2,4,7,4,9)
print(data.count(4))
print(data.index(4))

#set Unique values
l=[2,2,5,7,5,9]
s=set(l)
print(f"{s} --->{len(s)} Unique values")

#9. Set common elements
s1={1,2,3,4}
s2={3,4,5,6}
print(s1&s2)#S1 intersection s2

#10.Dictionary -Basic Lookup
students_marks={
"Ravi":82,
"Anu":91,
"Kiran":76
}
print(students_marks["Ravi"])


#MEDIUM PHASE
#11.List second largest

l=[10,4,8,10,6,9]
f1=0
s2=0
for num in l:
    if num>f1:
        f1=num
    elif s2<num<f1:
        s2=num
print(s2)

#list move zeros
nums=[0,1,0,3,12]
l1=[]
l2=[]
for num in nums:
    if num !=0:
        l1.append(num)
    else:
        l2.append(num)
print(l1+l2)

#13.Rotate list
l=[1,2,3,4,5]
k=2
last=l[-2:]
first=l[:-k]
print(last+first)
print("****************************")
#Another approach
l=[1,2,3,4,5]
k=2
k=k%len(l)
result=l[-k:]+l[:-k]
print(result)

#14. List -Frequency Table
nums=[2,3,2,4,3,2]
freq={}
count=0
for num in nums:
    if num in nums:
        freq.append(num:count)
        count+=1
print(f"{num}:{count}") 
#15.List of lists--Row sums
l=[[1,2,3],[4,5,6],[7,8,9]]
row_sum=[]
for row in l:
    row_sum.append(sum(l[0]))
print(sum)