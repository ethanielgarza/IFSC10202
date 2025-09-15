n = int(input("Enter Number: "))
sum = 0
for i in range(1,n+1):
    c = i ** 3
    sum = sum + c
    print(" ", i ,"cube", c)
print("The sum of ", sum)
