sequencesum = 0
sequencecount = 0
value = input("Enter a Number (CR to Quit): ")
while value != '':
    sequencesum += int(value)
    sequencecount += 1
    value = input("Enter a Number(CR to Quit): ")
if sequencecount != 0:
    sequenceaverage = sequencesum / sequencecount
    print("Average : {}".format(sequenceaverage))
else:
    print ("Sequence Length is 0")