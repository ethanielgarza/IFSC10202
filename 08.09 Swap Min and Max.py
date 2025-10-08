input_string = input("Enter Values Separated by Spaces: ")
string_list = input_string.split()
integer_list = []
for i in range(len(string_list)):
    integer_list.append(int(string_list[i]))
min_val = integer_list[0]
max_val = integer_list[0]
min_index = 0
max_index = 0

for i in range(len(integer_list)):
    if integer_list[i] < min_val:
        min_val = integer_list[i]
        min_index = i
    if integer_list[i] > max_val:
        max_val = integer_list[i]
        max_index = i

temp = integer_list[min_index]
integer_list[min_index] = integer_list[max_index]
integer_list[max_index] = temp

print("Swapped Minimum and Maximum:", *integer_list)