user_input = input("Enter a value separated by spaces: ")
values_list = user_input.split()
for i in range(1, len(values_list), 2):
    print(values_list[i])