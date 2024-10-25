# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriedns = ["Yousef", "Ahmed", "Hany", "Mohamed"]

myFriedns.append("Safwan")

print(myFriedns)

print(myFriedns.index("Safwan"))

myOldFriends = ["Samy", "3bqarino"]

myFriedns.append(myOldFriends)

print(myFriedns[-1])
print(type(myFriedns[-1]))   # List

print(myFriedns[-1][1])



# extend()

a = [1, 2, 3, 4]
b = ['A', 'B', 'C', 'D']
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# a.extend(b.extend(c))   => error


# remove()

var = [1, 2, 3, "One", "Two", True, False]
var.remove(2)
print(var)


# sort()

nums = [1, -4, 52, 31, -40, 21]
nums.sort()
print(nums)

alpha = ['a', 'b', 'n', 't']
alpha.sort(reverse = True)
print(alpha)


# reverse()

alpha.reverse()
print(alpha)


# clear()

a.clear()
print(a)


# copy()

list1 = [1, 2, 3, 4]
list2 = list1.copy()   # shallow copy isn't affected by the change of the main list
list1.append(5)
print("List #1: {}\nList #2: {}".format(list1, list2))


# count()

dig = [1,2, 5, 3, 7, 4, 12, 27, 13, 17, 2, 5, 12, 2]
print(dig.count(2))


# index()

print(dig.index(27))


# insert()

list3 = [1, 2, 3, 'a', 'b', 'c']
list3.insert(3, 4)
print(list3)


# pop()

print(list3.pop(4))
print(list3)