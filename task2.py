nameList = ("Lebron","Kobe","Michael","Shaq","Dennis")
a = input("enter name")
for i in nameList:
    if i == a:
        print("That name is in the list") 
if a not in nameList:
        print("That name is not in the list")
       
