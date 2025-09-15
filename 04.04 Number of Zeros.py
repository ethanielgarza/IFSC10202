number = int(input("Enter a number: "))
count = 0
while number != 0:
    if number % 10 == 10:
        count += 1
    number = number // 10
print("Count of zeros is : ", count)