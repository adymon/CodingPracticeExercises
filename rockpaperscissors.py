"""
Description:
!!!ROCK!!!
###PAPERS###
***SCISSORS***
s beats p beats r, r beats s
Usage:
>>Enter your choice : rock
You Choose: rock
Computer Choose: paper
Computer wins
User total win count is : 0
Computer total win count is : 1
>>Enter your choice:
"""
from random import randint

print("@@@ Welcome @@@ \n !!!ROCK!!! \n" + "###PAPERS### \n" + "***SCISSORS*** \n")

# Defining the total winning score count needed to win the game
user_wins = 0
computer_wins = 0
win_score = 2

# Repeat the game until either User or the computer wins the game
while user_wins < win_score and computer_wins < win_score:

    r = randint(0, 2)

    user = input("Enter your choice : ").lower()

    print(f"You Choose: {user}")

    if r == 0:
        computer = "rock"
    elif r == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer Choose: {computer}")

    if user == computer:
        print('it\'s a tie')
    elif user == 'rock':
        if computer == 'paper':
            print("Computer wins")
            computer_wins += 1
        else:
            print("User Wins")
            user_wins += 1

    elif user == 'paper':
        if computer == 'rock':
            print("User Wins")
            user_wins += 1
        else:
            print("Computer Wins")
            computer_wins += 1
    elif user == 'scissors':
        if computer == 'rock':
            print("Computer Wins")
            computer_wins += 1
        else:
            print("User Wins")
            user_wins += 1
    else:
        print("ATTENTION : Wrong input given by the User\n")
        qt = input("Want to quit the game? yes or no?\n").lower()
        if qt == 'yes':
            print("See You Again!")
            break
        else:
            continue

    print(f"User total win count is : {user_wins} \nComputer total win count is : {computer_wins}")
print(f"FINAL SCORE: \nUser total win count is : {user_wins} \nComputer total win count is : {computer_wins}")

