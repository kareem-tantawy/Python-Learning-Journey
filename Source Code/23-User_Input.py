#----------------#
#-- User Input --#
#----------------#

fName = input("What is your first name? ")
mName = input("What is your middle name? ")
lName = input("What is your last name? ")

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print("Hello {:s} {:.1s}. {:s}!\nGood to see you!".format(fName, mName, lName))