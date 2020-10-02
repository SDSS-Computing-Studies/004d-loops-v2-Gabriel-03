n = int(input("Enter a number\n"))
a = 0
for x in range(1,n+1):
    a = a + int("1" * x)
print("the sum of the series is " + str(a))
