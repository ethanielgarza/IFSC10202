# Function to print a two-dimensional list
def print_list(a):
    for row in a:
        for element in row:
            print(element, end=" ")
        print()

# Function to multiply every value in a list by a scale factor
def scale_list(a, s):
    scaled_a = []
    for row in a:
        new_row = []
        for element in row:
            new_row.append(element * s)
        scaled_a.append(new_row)
    return scaled_a

# Main program execution
if __name__ == "__main__":
    # Read the values from the file with error handling
    numbers_list = []
    try:
        with open('09.03 NumbersList.txt', 'r') as file:
            for line in file:
                row = [int(num) for num in line.strip().split()]
                numbers_list.append(row)
    except FileNotFoundError:
        print("Error: The file '09.03 NumbersList.txt' was not found.")
        exit()
    except ValueError:
        print("Error: The file contains non-numeric data.")
        exit()

    # Print the original list
    print("Original list:")
    print_list(numbers_list)

    # Prompt for a scale factor with error handling
    while True:
        try:
            scale_factor = float(input("Enter scale value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Multiply every value in the list by the scale factor
    scaled_list_result = scale_list(numbers_list, scale_factor)

    # Print the scaled list
    print("\nScaled list:")
    print_list(scaled_list_result)
