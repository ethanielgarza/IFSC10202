string1 = input("Enter a String: ")
spacecount = string1.count(' ')
if string1.strip() == "":
    num_of_words = 0
else:
    num_of_words = spacecount + 1
print(f"{num_of_words} words")