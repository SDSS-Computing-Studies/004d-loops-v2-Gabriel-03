number = int(input("Enter a number: "))
a = str(number)
b = 1 

for i in range(1, number+1):
    b = b*i
    
b = str(b)
print(a + "! is " + b)
