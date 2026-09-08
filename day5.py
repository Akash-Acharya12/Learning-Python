#Tuples
tuple1=("Akash",)
tuple2=("Acharya",)
tuples=tuple1+tuple2
print(tuples)
t1=(1,2,3,4)
t2=(5,6,7)
t=t1+t2
print(t*3)
print(6 in t2)
print(t.count(5))
print(t.index(6))

#Sets
s={1,2,34,55, 64}
print(type(s))
s1={1,2,3,}
s2={3,4,5}
s3=s1&s2#intersection

print(s3)
s4=s1|s2#Union
print(s4)
print(s1-s2)
m={1,2,3,4,5,}
m.add(6)
print(m)
m.remove(1)
print(m)
m.discard(1)
print(m)
print(m.pop())


list=["Akash","Dakshin","Yashwin","Koushik"]
list[0]="Adarsh"
print(list)
list.append("Chetan")
list.insert(5,"Kishan")
print(list)
print(list[2:4])


tuple=("Akash","Dakshin","Yashwin","Koushik")
print(tuple[2:4])
t1=(1,2,3)
t2=(3,4,5,6)
t=t1+t2
print(t)


s1={"Guva","Mango","Orange"}
s2={"Sapota","pomogranet","Dragon fruit","Guva"}
print(s1|s2)
print(s1&s2)
print(s1-s2)
s1.add("Graps")
s2.remove("pomogranet")
s2.discard("Sapota")
print(s1,s2,)



#Tuple and Set comparison

My_list=[1,2,3,4,5,6]
'''
tup=tuple(My_list)
print(tup)
'''
s=set(My_list)
print(s)