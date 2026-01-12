#print("o----""\n")
#print(" ||||")
#print("Jesus is KING\n")
#print('*' * 15) #Expression

#Variables
#price = 10
#rating = 2.5
#name = "Reacher"
#divison = price // 5
#print(price)
#is_published = False

# Hostiptal 
#Name = 'John Smith'
#age = 20
#Patient_status = True


#print("A journey begins with faliure, and with ever faliure, becomes a greater man!")


print('Winners and Losers - Human is Even, Computer is Odd')

humanscore = 0
computerscore = 0

for i in range(1,6):
    print(f"Round: {i}")

    human_guess = int(input("Enter a guess: "))


    from random import randint
    computer_guess = randint(1,6)
    sum = computer_guess + human_guess

    print("Human Guess: {}".format(human_guess) + " Computer Guess: {}".format(computer_guess))

    #Calculations

    if sum % 2 == 0:
        humanscore += 1 
        print("Sum is Even")
    else:
        computerscore += 1
        print("Sum is Odd")
    computerwins = sum % 2 != 0
    
if human_guess > computer_guess:
    print("Human Wins")
if computer_guess > human_guess:
    print("Computer Wins")