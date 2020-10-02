nameList = ("Lebron","Kobe","Michael","Shaq","Dennis")
a = input("Enter a name: ").strip()
for i in nameList:
    if i == a:
        print("That name is on the list")
        
if a not in nameList:
        print("That name is not on the list")
