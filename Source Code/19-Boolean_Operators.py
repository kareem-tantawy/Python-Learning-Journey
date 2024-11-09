# ----------------------- #
# -- Boolean Operators -- #
# ----------------------- #

# -----------------------
# and  &
# or   |
# not  !
# -----------------------

# and (&)
print(True & True)   # True
print(True & False)  # False
print(False & False) # False
print(False & True)  # False

# We can also use the keyword 'and' instead of '&'
print(True and True)   # True

age = 23
country = "Egypt"
rank = 9.8

print(age > 18 and country == "Egypt" and rank < 5)  # False


print('*' * 50)


# or (|)
print(True | True)   # True
print(True | False)  # True
print(False | False) # False
print(False | True)  # True

# We can also use the keyword 'or' instead of '|'
print(True or True)   # True

print(age > 18 or country == "Egypt" or rank < 5)  # True


print('*' * 50)


# not (!)
print(not True)   # True
print(not False)  # True

print(age > 18 and country == "Egypt" and (not rank < 5))  # True