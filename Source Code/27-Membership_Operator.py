# -------------------------- #
# -- Membership Operators -- #
# -------------------------- #

# in
# not in
# --------------------------

# String

name = "Karim"

print('K' in name)
print('a' not in name)


print('='*30)


# List

friends = ["Yousef", "Ahmed", "Mohamed", "Hany"]
print("Mohamed" not in friends)


print('='*30)


# Using In and Not In with Conditions

countriesOne = ["Egypt", "Palestine", "KSA", "Emarat", "Kuwait", "Bahrain"]
countriesOneDiscount = .8

countriesTwo = ["Turkey", "Italy", "Russia", "Chiana"]
countriesTwoDiscount = .3

myCountry = "Turkey"

if myCountry in countriesOne:
    print(f"Hello, You Got a Discount = {countriesOneDiscount*100:.0f}%")
elif myCountry in countriesTwo:
    print(f"Hello, You Got a Discount = {countriesTwoDiscount*100:.0f}%")
else:
    print(f"Hello, You Got a Discount = {.15*100:.0f}%")
    