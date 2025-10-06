x = input("enter values separated by spaces: ")
a = x.split()
indexofmax = 0
for i in range(1, len(a)):
    if int(a[i]) > int(a[indexofmax]):
        indexofmax = i 
print("Largest value: {}".format(a[indexofmax]))
print("index of largest value: {}".format(indexofmax))