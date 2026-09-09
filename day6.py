#dictionaries
birthday={
 "Akash":"3-9-2007",
 "yashwin":"27-10-2007",
 "Koushik":"2-1-2007"
  }
print(birthday)
print(birthday["Akash"])
print(birthday.get("Madhu","not found"))
birthday["Adarsh"]="4-1-2008"
print(birthday)
birthday["Akash"]="2-9-2007"
print(birthday )
x=birthday.pop("Akash")
print(birthday)
print(x)
del birthday["yashwin"]
print(birthday.keys())
print(birthday.values())
print(birthday.items())
b2={
"Madhu":"3-5-2007",
"koushal":"4-5-2007",
"Tanzz":"6-2-2007"
}
birthday.update(b2)
print(birthday)
dic={
23:67,
(12,"my"):67,
"list":["l1","l2","l3"]
}
print(dic)

i1={
"name":"Milk",
"weight":1,
"price":50
}
i2={
"name":"Sugar",
"weight":2,
"price":40
}
items=[i1,i2]
print(items)
items=(i1,i2)
print(items)
items=i1,i2
print(items)

print(f"Total weight: {i1["weight"]+i2["weight"]} kg")

dishes={
"Madikeri":"Pandi kari",
"mangalore":"fish",
"Davangere":"Bennedosa",
"mysore":"Mysore pak",
"XYZ":"Ragi"
}
dishes["udupi"]="Dosa"
print(dishes)
dishes["mangaluru"]="neerdosa"
print(dishes)
dishes.pop("mysore")
print(dishes)

d1={
"name":"Adarsh",
"f_s":"Maths",
"f_f":"pups"
}
d2={
"name":"Yashwin",
"f_s":"Kannada",
"f_f":"biriyani"
}
print(f"{d1["name"]} favorite food is {d1["f_f"]} ")