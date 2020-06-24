from random import randint

# list of play options
play = ["Rock", "Paper", "Scissors"]

# list of messages
messages = ["Tie!", "You win!", "You lose!"]

# game rule
winning_rule = {"Rock": "Scissors", "Paper": "Rock", 
                "Scissors": "Paper"}

while True:
    
    # get the user input
    player = input("Rock, Paper, Scissors? ")
    
    # quit
    if player not in winning_rule:
        break
    
    # assign a random play to the computer
    computer = play[randint(0, 2)]
    print('Computer: {}'.format(computer))
    
    # tie
    if player == computer:
        print(messages[0])
    
    # you win
    elif winning_rule[player] == computer:
        print(messages[1])
    
    # you lose
    else:
        print(messages[2])
    
    # new line
    print()

# bye
print("Bye!") 
