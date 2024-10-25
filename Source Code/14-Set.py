# --------- #
# -- Set -- #
# --------- #

# -----------------------------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Can't Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples)
#     List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed

mySetOne = {"Karim", "Tantawy", 10}
print(mySetOne)
# print(mySetOne[0])  => error


# Slicing Can't be Done

mySetTwo = {1, 2, 3, 4, 5}
# print(mySetTwo[1,3])  => error


# Has Only Immutable Data Types

# mySetThree = {"Karim", True, 10.2, 15, [12, 17], 9}  # unhashable type: 'list'
mySetThree = {"Karim", True, 10.2, 15, (12, 17), 9}

print(mySetThree)


# Items are Unique

mySetFour = {1, 2, "Karim", "Tantawy", 2, "Tantawy"}
print(mySetFour)  # {1, 2, 'Karim', 'Tantawy'}
