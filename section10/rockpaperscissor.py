from random import randint
choice = ["rock","paper","scissors"]

player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    p1 = input("Player: choose rock,paper or scissors ").lower()
    if p1 == "quit" or p1 == "q":
        break
    ai = choice[randint(0,2)]

    print(f"Computer played {ai}")
    if p1 == ai:
        print("It's a tie!")
    elif p1 == "rock":
        if ai == "scissors":
            print("Player1 wins")
            player_wins +=1
        elif ai == "paper":
            print("Computer wins")
            computer_wins += 1
    elif p1 == "paper":
        if ai == "rock":
            print("Player1 wins")
            player_wins +=1
        elif ai == "scissors":
            print("Computer wins")
            computer_wins += 1
    elif p1 == "scissors":
        if ai == "paper":
            print("Player1 wins")
            player_wins +=1
        elif ai == "rock":
            print("Computer wins")
            computer_wins += 1

    else:
        print("Something went wrong")
if player_wins > computer_wins:
    print("CONGRATS, YOU WON!!")
elif player_wins == computer_wins:
    print("ITS A TIE")
else:
    print("OH NO :( , THE COMPUTER WON...")