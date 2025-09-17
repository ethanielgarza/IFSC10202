value = input("Enter a Number (CR to quit): ")
if value != "":
    maxium = int(value)
    while value != "":
        if int(value) > maxium:
            maxium = int(value)
        value = input("Enter a Number (CR to Quit): ")
    print("Maxium: {}" .format(maxium))
else:
    print("Sequence Length is 0")
if value != "":
    index = int(value)
    while value != "":
        if int(value) == maxium:
            maxium = index
        value = input("Enter a Number (CR to Quit): ")
    print("Index: {}" .format(index))