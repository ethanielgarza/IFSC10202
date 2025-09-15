N = int(input("Enter a Max Height: "))
for i in range (N-1):
    for j in range (1+i):
        print("*", end=" ")
    print()
for i in range (N):
    for j in range(N-i):
        print("*", end=" ")
    print()