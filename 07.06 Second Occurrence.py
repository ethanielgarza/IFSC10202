user_input = input("Enter a String: ")
first_index = user_input.find('f')

if first_index != -1:
    second_index = user_input.find('f', first_index + 1)
    if second_index != -1:
        print(second_index)
    else: 
        print("One f")
else:
    print("Zero f")