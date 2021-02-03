print("...rock...")
print("...paper...")
print("...scissors...")
p1 = input("Enter Player 1's choice)")
p2 = input("Enter Player 2's choice)")

# rock > scissors > paper
if p1 == p2:
    print("It's a tie!")
elif p1 == "rock":
    if p2 == "scissors":
        print(f"SHOOT\n player1 wins")
    elif p2 == "paper":
        print(f"SHOOT\n player2 wins")
elif p1 == "paper":
    if p2 == "rock":
        print(f"SHOOT\n player1 wins")
    if p2 == "scissors":
        print(f"SHOOT\n player2 wins")
elif p1 == "scissors":
    if p2 == "paper":
        print(f"SHOOT\n player1 wins")
    if p2 == "rock":
        print(f"SHOOT\n player2 wins")
else:
    print("Something went wrong")



