import random

flags = False

while True:
    computer_number = random.randint(1, 100)
    while True:
        player_guess = input("Guess the number (1, 100): ")
        if int(player_guess):
            pass
        else:
            print("Invalid input. Try again.")
            continue
        player_int = int(player_guess)
        if player_int == computer_number:
            print("You guessed the number!")
            print()
            again = input("Play again? Y/N: ")
            if again.lower() == "y":
                print()
                break
            if again.lower() == "n":
                raise SystemExit("Thanks for playing!")
        else:
            print("Try again!")
            if player_int > computer_number:
                print("Too high!")
            else:
                print("Too low!")
            print()
        flags = False
