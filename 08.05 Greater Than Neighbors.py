x = input("enter values separated by spaces: ")
count = 0 
a = x.split()
for i in range(1, len(a)- 1):
    if int(a[i]) > int(a [i + 1]) and int(a[i]) > int(a [i - 1]):
        count += 1
print(count)