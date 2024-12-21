# ------------------------- #
# -- Built-in funcations -- #
# ------------------------- #
# all()       => checks if all elements are true in a list
# any()       => checks if any element is false in a list
# bin()       => returns the binary
# id()        => returns the id
# sum()       => returns the summition of sevral elements
# round()     => rounds the floating point number to any number after the decimal
# range()     => generates a sequence of numbers within a specified range.
# print()     => displays output to the console or other standard output device.
# abs()       => returns the absluate value
# pow()       => returns the result of number raised to a power of another number
# min()       => returns the minimum value
# max()       => returns the maximum value
# slice()     => creates a slice object representing a set of indices for extracting a portion of a sequence (like strings, lists, tuples).
# enumerate() => adds a counter to an iterable and returns it as an enumerate object (pairs of index and value).
# help()      => invokes the built-in help system to get documentation on objects, modules, functions, etc.
# reversed()  => This function returns a reverse iterator for the given sequence.
# ---------------------------------------------------------------------------------------------------------------------------------------

myList = [0, 1, 2, 3, 4]

# all()
if all(myList):
    print("All elements are true")
else:
    print("There is at least one element false")


print("*" * 50)

# any()
if any(myList):
    print("There is at least on true value in the list")
else:
    print("All elements are false")

print("*" * 50)

# bin()
print(bin(100))


print("*" * 50)

# id()
a, b = 1, 2

print(id(a))
print(id(b))


print("*" * 50)

# sum()
myList = [3, 7, 15, 12]
print(sum(myList))
print(sum(myList, 10))


print("*" * 50)

# round(num, numOfDigits)
print(round(78.15))
print(round(78.15, 1))


print("*" * 50)

# range(start, end, step)
#        no   must   no
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(1, 5, 2)))

for i in range(5):
    print(i)

print("*" * 50)

# -- print() -- #

# sep   its default value is ' '
print("Hello Python")
print("Hello", "Python", sep="*")

# end   => its default value is '\n
print("First Line", end=" ")
print("Second Line")
print("Third Line", end="")


print("*" * 50)

# abs()
print(abs(-50))


print("*" * 50)

# pow()
print(pow(5, 3))
print(pow(5, 3, 2))  # == 125 % 2


print("*" * 50)

# min()
print(min(15, 31, 5131, 2, 51, -1))
print(min("g", "Karim", "m", "a"))


print("*" * 50)

# max
print(max(15, 31, 5131, 2, 51, -1))
print(max("g", "Karim", "m", "a"))


print("*" * 50)

# slice()
myList = ["a", "b", "c", "d", "n", "p", "j"]

print(myList[:4])
print(myList[slice(4)])


print("*" * 50)

# enumerate(iterable, start = 0)
mySkills = ["C++", "HTML", "Python"]

for skill in mySkills:
    print(skill)

print("*" * 10)

mySkillShow = enumerate(mySkills, 2)

print(type(mySkillShow))

for skill in mySkillShow:
    print(skill)


print("*" * 10)

for index, skill in enumerate(mySkills, 1):
    print(f"{index}- {skill}")


print("*" * 50)


# help()
print(help(print))


print("*" * 50)


# reversed()
name = "Karim"

print(reversed(name))

for letter in reversed(name):
    print(letter)


print("*" * 10)


for skill in reversed(mySkills):
    print(skill)
