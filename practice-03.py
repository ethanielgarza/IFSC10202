grade = float(input("Enter your Score (0-100): "))

# font color change
print ("=" *40)
RED = "\033[31m"
RESET = "\033[0m"
print( RED + "GRADE REPORT"+ RESET)
print ("=" *40)
print(f"Score: {grade}")

#Invaild number if statement
if grade < 0 or grade > 100:
    print("Please enter a grade vaild between 0 to 100")
else:
    if grade >= 90:
        print("Grade: A\nFeedback: Excellent Work!")
    elif grade >= 80:
        print("Grade: B\nFeedback: Good Job!")
    elif grade >= 70:
        print("Grade: C\nFeedback: Keep Working Hard!")
    elif  grade >= 60:
        print("Grade: D\nFeedback: You can Improve!")
    else:
        print("Grade: F\nFeedback: Lets work together to Improve!")



"""
Program 02
"""

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))

def add_numbers (num1, num2):
    return num1 + num2

def multiply_numbers (num1, num2):
    return num1 * num2

def is_even (num):
    return num % 2 == 0

def calculate_average (num1, num2):
    return (num1 + num2) / 2

#calling Functions
total = add_numbers(num1, num2)
product = multiply_numbers(num1, num2)
avg = calculate_average(num1, num2)

num1_Even = is_even(num1)
num2_Even = is_even(num2)

# print statements
# font color change
print ("=" *40)
RED = "\033[31m"
RESET = "\033[0m"
print( RED + "Math Helper Results"+ RESET)
print ("=" *40)
print(f"Numbers: {num1} and {num2}")
print(f"Sum: {total}")
print(f"Is {num1} Even?: {num1_Even} ")
print(f"Is {num2} Even?: {num2_Even} ")
print(f"Average of {num1} and {num2}: {avg}")