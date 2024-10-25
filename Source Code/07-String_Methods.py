
# --------------------------- #
# - Strings Methonds Part 1 - #
# --------------------------- #

# len => Get Length
myStr1 = "My Name Is Kareem"
print(len(myStr1))


# strip => Truncating spaces (or any chosen ones) from left or right or both
myStr2 = "   My Name Is Kareem   "
print(myStr2.rstrip()) # length = 20
print(myStr2.lstrip()) # Length = 20
print(myStr2.strip())  # Length = 17

myStr3 = "#$## My Name Is Kareem ###"
print((myStr3.strip("# $")))


# title() => Give special printing formats
myStr4 = "I love python, and 3d Graphics"
print(myStr4.title())


# capitalize() => Make the first char capital
myStr5 = "i love Python, And 3d Graphics"
print(myStr5.capitalize())


# zfill => Numbering with zeros
a, b, c = '3', '99', '125'
print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))


# upper() => change all chars to uppercase
myStr6 = "Kareem"
print(myStr6.upper())


# lower() => change all chars to lowercase
myStr7 = "KAreem"
print(myStr7.lower())



print("*************************")



# split(), rsplit()   splits the words by any char you want
myStr1 = "I love Python"
print(myStr1.split())       # Automatically split by space

print(type(myStr1.split()))

a, b, c = myStr1.split()
print(a)
print(b)
print(c)

myStr2 = "I-love-Python-and-C++"
print(myStr2.split('-'))

myStr3 = myStr2
print(myStr3.split('-', 2))

print(myStr3.rsplit('-', 3))


# center()  Give a special print by adding symbols at the start and the end
name = "Kareem"
print(name.center(10))
print(name.center(10, '*'))


# count()  counts specific word in a string
msg = "My name is Kareem Tantawy"
print(msg.count("Kareem"))
print(msg.count("Kareem", 0, 10))


# swapcase()  swap uppercase to lowercase and the opposite 
first = msg
print(first.swapcase())


# startwith()  return true or false
middle = msg
print(middle.startswith('M'))
print(middle.startswith("A"))
print(middle.startswith('n', 3, 15))



print("*************************")


# endwith()  return true or false
middle = msg
print(middle.endswith('y'))
print(middle.endswith("A"))
print(middle.endswith('K', 3, 12))


# index()
msg2 = "I love to learn Python"
print(msg2.index('P'))
# print(msg2.index('P', 3, 15))    => Error


# find()
msg2 = "I like to learn Python"
print(msg2.find('P'))
print(msg2.find('P', 3, 15))    # If not exist it thorws -1



# rjust(width, fill char), ljust(width, fill char)
n = "Kareem"
print(n.rjust(8))
print(n.ljust(8, '&'))


# splitlines()

e = """First line 
Second line 
Third line"""
print(type(e.splitlines()))

x, y, z = e.splitlines()
print(x)
print(y)
print(z)


# expandtabs()
t = "Hello\tI\tlove\tPython"
print(t.expandtabs(3))


# replace (old value, new value, count)

rep = "One Two Three Four Five One"

print(rep.replace("One", '1'))
print(rep.replace("One", '1', 1))


# join()
myList = ["Kareem", "Ahmed", "Tantawy"]
print(", ".join(myList))


print("#####################")


# Appling for the built in functions
Title = "My Name Is Kareem"
print(Title.istitle())  # title() => Give special printing formats


spacing = " "
print(spacing.isspace())

lower = "i love python"
print(lower.islower())  # Same as isupper() but in the opposite format

indent = "3Name"
print(indent.isidentifier())

alpha = "Kareem01"
print(alpha.isalpha())  # False bucause '01' is not an alpha 'a-z'

alnum = alpha
print(alnum.isalnum())  # True because alnum is including numbers and letters



