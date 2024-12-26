# Guess The Number
# You will have to guess a number from 1 to 10

import random
import pyfiglet
import termcolor


flag = True

while flag:
    secret = random.randint(1, 10)
    for i in range(3):
        guess = int(
            input("I'm thinking of a number between 1 and 10. Can you guess it? ")
        )
        if guess == secret:
            print(
                termcolor.colored(
                    pyfiglet.figlet_format("Congratulations, you guessed it!"),
                    color="green",
                )
            )
            break
        if i == 2:
            continue
        if guess > secret:
            print("Nope, your guess is a bit high. Give it another shot!")
        else:
            print("Nope, your guess is a bit low. Give it another shot!")
    else:
        print(
            termcolor.colored(
                pyfiglet.figlet_format("Oops, you've finished your 3 tries"),
                color="red",
            )
        )
    msg = input("Wanna play again? (yes/no) ")
    if msg == "y" or msg == "yes":
        flag = True
    elif msg == "n" or msg == "no":
        flag = False
    else:
        print("Please enter a valid input")
        msg = input("Wanna play again? (yes/no) ")
        if msg == "y" or msg == "yes":
            flag = True
        elif msg == "n" or msg == "no":
            flag = False
        else:
            print(
                "Sorry, you inputed wrong input twice, I have to terminate the program"
            )
            break
