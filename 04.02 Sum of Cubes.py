def sumcube(n):    #defining the function
    sum = 0         #constant
    while(n > 0):   #checking the condition
        x = n % 10  #will result the remainder
        sum = sum + (pow(x,3))  #3 is the power of the cube
        n = n // 10 #result in the qoutient
    print("Sum of cubes: ", sum)
n = int(input("Enter Number: "))
sumcube(n)