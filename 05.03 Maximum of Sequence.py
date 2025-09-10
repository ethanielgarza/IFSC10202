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