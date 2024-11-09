# ---------------------------- #
# -- Loop => While Training -- #
# -- Simple Password Guess  -- #
# ---------------------------- #


password = "karim@123"

tries = 3

userPassword = input("Enter your password please: ")

while userPassword != password:
    print(f"This is your {4 - tries if tries > 1 else "last"} chance!")
    tries -= 1
    userPassword = input("Enter your password please: ")
    if tries == 0:
        print("Sorry, We need to terminate the program!")
        break
    
else :
    print("Correct Password!")