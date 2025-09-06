number1 = float(input("Enter First Number: "))
operator = input("Enter a operator (+,-,*,/): ")
number2 = float(input("Enter Second Number: "))

result = None

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    print("Invalid Operator")
if result is not None:
    print(f"{number1} {operator} {number2} = {result}")