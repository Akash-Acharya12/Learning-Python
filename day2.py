#String manipulation Exercise

sen=input("Enter a sentence: ")
upper=sen.upper()
print(f"Uppercase: {upper}")
lower=sen.lower()
print(f"Lowercase: {lower}")
replace=sen.replace(" ", "_")
print(f"Replaced:",replace)
print(f"stripped {sen.strip()}")

 
 
 #Character counter excluding space

stri=input("Enter a string: ")
spr=stri.replace(" ","")
print(f"number of Characters ;{len(spr)}")



#Concatination and Repitition

F_name=input("Enter your name: ")
L_name=input("Enter your last name: ")
full_name=F_name+" " +L_name
print(f"Full name={full_name}")

#Repitition
name="Akash "*3
print(name *2)

name= "Akash"
replaced=name.replace("Akash","Dakshin")
print(replaced)

#Multiline string'
#sentence= '''Hello My name is '' akash''  a 2nd year engineering student
#                     and my Friend name is "dakshin" '''
#print(sentence)

#print("Hello \n \t World \n This is a Backslash")