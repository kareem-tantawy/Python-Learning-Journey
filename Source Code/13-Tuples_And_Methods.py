# ------------ #
# -- Tuples -- #
# ------------ #

# ------------------------------------------------------------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want 
# [3] Tuples Are Ordered, To Use Index To Access Items
# [4] Tuples Are Immutable => You Can't Add or Delete
# [5] Tupls Items Isn't Unique
# [6] Tuples Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# ------------------------------------------------------------


# Tuple Syntax & Type Test
 
myTupleOne = ("Karim", "Ahmed", "Tantawy")
myTupleTwo = "Karim", "Ahmed", "Tantawy"

print(myTupleOne)
print(type(myTupleTwo))


# Tuples With One Element

TupOne = tuple("Karim")
TupTwo = "Karim",
print(type(TupOne))
print(type(TupTwo))


# Tuple Indexing

myTupleThree = (1, 2, 3, 4, 5)
print(myTupleThree[0])
print(myTupleThree[-1])


# Tuple Assign Values

myTupleFour = (1, 2, 3, 5, 9, 21)
# myTupleFour[2] = 4                  #'tuple' object does not support item assignment


# Tuples Items

myTupleFive = ("Karim", 3, 'T', False, 5.12)
print(myTupleFive)


# Tuples Concatenation

a = (1, 2, 3, 4)
b = (4, 5, 6)
c = a + b + (7, 8, 9)
print(c)


# Tuple, List, String Repeat (*)

myString = "Kareem"
myList = [1, 2]
myTupleSix = ("A", "B")

myTupleSeven = myTupleSix*2

print(myString*3)
print(myList*3)
print(myTupleSix*3)
print(myTupleSeven*1)


#-------------#
# --Methods --#
# ------------#

# count()

myTupleEight = (1, 2, 3, 1, True, "Karim", False, 2, 1, "Tantawy", 4.25)
print(myTupleEight.count(1))     # 4 => Because of 'True'


# index()
inde = 2
print(f"The Position of [{myTupleEight[inde]}] is: {myTupleEight.index(myTupleEight[inde])}")


# Tuple Destruct

myTupleNine = 'a', 5, 'b', 'c'
x, _, y, z = myTupleNine

print(x)
print(y)
print(z)
