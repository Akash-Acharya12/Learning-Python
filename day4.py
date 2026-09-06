#LISTS
items=["Ragi","Maida","Wheet","chat"]
items.reverse()
print(items)
items.remove("Ragi")

print(items)
items[0]="maida"
items.append("garam")
print(items)
cutted=items[0::2]
print(cutted[0])
l1=[1,2,3,4]
l2=[5,6,7]*3
l=l1+l2
print(l*3)