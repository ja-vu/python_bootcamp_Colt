from random import randint

number = randint(1,10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("You won")
        play_again=input("Do you want to play again? (y/n) ").lower()
        if play_again == "y":
            number = randint(1, 10)
            guess == None
        else:
            print("Thank you for playing")
            break