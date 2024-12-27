# -------------------------- #
# -- Iterable vs Iterator -- #
# -------------------------- #
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

name = "Karim"

for letter in name:
    print(letter, end=" ")

print(end="\n")

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == numbers[-1]:
        print(number)
    else:
        print(number, end=", ")


print("*" * 20)

# Doing the same but with iterators {iter(), next()} methods

# creating iterator using iter() method
myName = iter(name)

# Iterating through myName variable using next() method
print(next(myName), end=" ")
print(next(myName), end=" ")
print(next(myName), end=" ")
print(next(myName), end=" ")
print(next(myName), end="\n")
# print(next(myName), end=' ')   # stopIteration because it's reached to the end

# creating iterator using iter() method
myNumbers = iter(numbers)

# Iterating through myNumbers variable using next() method
print(next(myNumbers), end=", ")
print(next(myNumbers), end=", ")
print(next(myNumbers), end=", ")
print(next(myNumbers), end=", ")
print(next(myNumbers), end="\n")
