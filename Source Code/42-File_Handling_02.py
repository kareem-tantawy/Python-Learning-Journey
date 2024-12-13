# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

import os

os.chdir(os.path.dirname(__file__))

file = open(r"e:\mohamed\plain.txt", "w")

file.write("Line one\n")
file.write("Line Two\n")
file.write("Line Three\n")

myFriends = ["Yousef\n", "Ahmed\n", "Mohamed\n", "Hany\n"]

friends = open(r"e:\mohamed\plain.txt", "a")

friends.writelines(myFriends)
