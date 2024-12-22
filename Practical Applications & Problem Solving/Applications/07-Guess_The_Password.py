# Guess The Number
# You will have to guess a number from 0 to 10

import random


flag = True

while flag:
    secret = random.randint(1, 10)
    for i in range(3):
        if i == 3:
            break
        guess = int(
            input("I'm thinking of a number between 1 and 10. Can you guess it? ")
        )
        if guess == secret:
            print("Congratulations, you guessed it!")
            break
        elif guess > secret:
            print("Nope, your guess is a bit high. Give it another shot!")
        else:
            print("Nope, your guess is a bit low. Give it another shot!")
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
