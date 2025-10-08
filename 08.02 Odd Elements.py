user_input = input("Enter a value separated by spaces: ")
values_list = user_input.split()

result_list = []
for value in values_list:
    number = int(value)
    if number % 2 != 0:
        result_list.append(value)

print(", ".join(result_list))
