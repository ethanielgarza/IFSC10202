input_string = input("Enter a value of separated by spaces: ")
values_as_strings = input_string.split()

values_as_integers = []
for i in range(len(values_as_strings)):
    values_as_integers.append(int(values_as_strings[i]))

unique_elements = []
for i in range(len(values_as_integers)):
    is_unique = True
    for j in range(len(values_as_integers)):
        if i != j and values_as_integers[i] == values_as_integers[j]:
            is_unique = False
            break
    if is_unique:
        unique_elements.append(values_as_integers[i])

print("Unique Elements:", end=" ")
for i in range(len(unique_elements)):
    print(unique_elements[i], end=" ")