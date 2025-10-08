user_input = input("Enter Values Separated by Spaces: ")
string_list = user_input.split()
num_list = []
for i in range(len(string_list)):
    num_list.append(int(string_list[i]))

# Swap adjacent items in pairs
# The loop increments by 2 to process pairs
# It stops before the last element if the list has an odd number of elements
for i in range(0, len(num_list) - 1, 2):
    # Swap elements using tuple assignment
    num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]

# Print the resulting list
print("Swapped Values:", end=" ")
for i in range(len(num_list)):
    print(num_list[i], end=" ")
