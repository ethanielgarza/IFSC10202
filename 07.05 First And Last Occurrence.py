user_input = input("Enter a String: ")
first_occurrence = user_input.find("f")
last_occurrence = user_input.rfind("f")
if first_occurrence == -1:
    print(0)
elif first_occurrence == last_occurrence:
    print(first_occurrence)
else: 
    print(first_occurrence, last_occurrence)