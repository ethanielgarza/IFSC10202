first = int(input("Enter Frist Number: "))
second = int(input("Enter Second Number: "))
third = int(input("Enter Third Number: "))
if first <= second and first <= third:
    leastamount = first 
elif second <= first and second <= third:
    leastamount = second
else:
    leastamount = third
print(leastamount)