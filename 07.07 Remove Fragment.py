user_text = input("Enter a string: ")
first_occurrence = user_text.find('h')
last_occurrence = user_text.rfind('h')
new_text = user_text[:first_occurrence] + user_text[last_occurrence + 1:]
print(new_text)