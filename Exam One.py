print('Winners and Losers - Human is Even, Computer is Odd')

humanscore = 0
computerscore = 0

for i in range(1,6):
    print(f"Round: {i}")

    human_guess = int(input("Enter a guess: "))


    from random import randint
    computer_guess = randint(1,6)
    sum = computer_guess + human_guess
    
    #dvision
    if sum % 2 == 0:
        humanscore += 1 
        print("Sum is Even")
    else:
        computerscore += 1
        print("Sum is Odd")
    computerwins = sum % 2 != 0

    print("Human Guess: {}".format(human_guess))
    print("Computer Guess: {}".format(computer_guess))
    