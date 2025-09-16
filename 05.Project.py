def count_digits(number):

    #Calculates the number of digits in an integer.

    if number == 0:
        return 1
    count = 0
    temp_num = abs(number)
    while temp_num > 0:
        temp_num //= 10
        count += 1
    return count

def is_special_number(number):

    #Checks if a number is a special number.

    if number < 0:
        return False  # Special numbers are typically positive
    
    original_number = number
    num_digits = count_digits(number)
    sum_of_powers = 0
    temp_num = number

    while temp_num > 0:
        digit = temp_num % 10
        sum_of_powers += digit ** num_digits
        temp_num //= 10
    
    return sum_of_powers == original_number

def find_special_numbers_in_range(start, end):

    #Finds and prints special numbers within a given range.

    print(f"Special Numbers between {start} and {end}")
    found_special_numbers = False
    for num in range(start, end + 1):
        if is_special_number(num):
            print(num)
            found_special_numbers = True
    
    if not found_special_numbers:
        print("No special numbers found in this range.")

 #Main program execution
if __name__ == "__main__":
    try:
        lower_bound = int(input("Enter Start of range: "))
        upper_bound = int(input("Enter End of range: "))

        if lower_bound > upper_bound:
            print("Error: Lower bound cannot be greater than the upper bound.")
        else:
            find_special_numbers_in_range(lower_bound, upper_bound)
    except ValueError:
        print("Invalid input. Please enter integers for the range bounds.")