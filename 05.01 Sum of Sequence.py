total_sum = 0
print("Enter a sequence of numbers, one per line. Press Enter on an empty line to finish.")

while True:
    user_input = input()
    if user_input == "":  # Check for an empty line (carriage return)
        break
    try:
        number = float(user_input)  # Convert input to a float to handle decimals
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a number or press Enter to finish.")

print(f"The sum of the numbers is: {total_sum}")