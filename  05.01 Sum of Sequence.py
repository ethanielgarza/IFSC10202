sequencesum = 0
value = input("Enter a Number (CR to Quit): ")
while value != '':
    sequencesum += int(value)
    value = input("Enter a Number (CR to Quit): ")
print("Sum {}".format(sequencesum))