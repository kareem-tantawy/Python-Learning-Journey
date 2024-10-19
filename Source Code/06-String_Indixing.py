# This Code is to train on indixing in strings

# ----------- #
# - Strings - #
# ----------- #

myString = "I love Python"

# Indixing single item
print(myString[0]) # => I

print(myString[-6]) # => P  (6th char from edn)

# Slicing (Access multiple sequence Itmes)
# [Start:End] *End not included!
# [Start:End:Steps]

print(myString[0:6]) # I love
print(myString[:6]) # I love    (Will start from 0 automatically)
print(myString[7:]) # Python    (Will stop at the end automatically)
print(myString[:]) # I love Python    (Will print all content automatically)
print(myString[2:13:2]) #lv yhn