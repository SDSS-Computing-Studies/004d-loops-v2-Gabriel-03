a = int(input("Enter a number: "))
sum = 0
for i in range(1,a+1):
    while i > 0:
        sum += 10**(i - 1)
        i -= 1
print("the sum of the series is " + str(sum))
