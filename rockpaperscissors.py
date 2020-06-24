from random import randint

# list of play options
play = ["Rock", "Paper", "Scissors"]

while True:

    # get the user input
    player = input("Rock, Paper, Scissors? ")
    
    # assign a random play to the computer
    computer = play[randint(0, 2)]
    print('Computer: {}'.format(computer))
    
    # tie
    if player == computer:
        print("Tie!")  
    
    # rock
    elif player == "Rock":
        if computer == "Scissors":
            print("You win!")
        else:
            print("You lose!")
    
    # paper
    elif player == "Paper":
        if computer == "Rock":
            print("You win!")
        else:
            print("You lose!")
    
    # scissors
    elif player == "Scissors":
        if computer == "Paper":
            print("You win!")
        else:
            print("You lose!")       
    
    # quit
    else:
        break

    # new line
    print()

# bye
print("Bye!") 