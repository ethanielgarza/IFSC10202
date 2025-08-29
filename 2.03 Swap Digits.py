number = int(input("enter a number: "))
unit = number % 10
tens = number // 10
new_number = unit*10 + tens
print(new_number)