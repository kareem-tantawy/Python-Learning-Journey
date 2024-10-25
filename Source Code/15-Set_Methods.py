# ----------------- #
# -- Set Methods -- #
# ----------------- #

# clear()
cle = {1, 2, 3, 5}
cle.clear()
print(cle)


print("*" * 50)


# union()

a = {1, 2, 3}
b = {"a", "b", "c"}
c = {True, False}
print(a | b)
print(a.union(b, c))
print(a.union(b.union(c)))


print("*" * 50)


# add()

k = {1, 2, 3, 4}
k.add(5)
k.add(6)
# k.add(5, 6)  => error, it takes only one arguement

print(k)


print("*" * 50)


# copy()

h = {"a", "b", "c"}
g = h.copy()  # shallow copy
i = h  # deep copy

h.add("d")

print(h)
print(g)
print(i)


print("*" * 50)


# remove()

one = {1, 2, 3, 4}
one.remove(2)
# one.remove(5)  => keyerror
print(one)


print("*" * 50)


# discard()    => same as remove but without an error message

one = {1, 2, 3, 4}
one.discard(2)
one.discard(5)
print(one)


print("*" * 50)


# pop()

p = {3, 2, True, False, "Name"}
print(p.pop())


print("*" * 50)


# update()

u = {1, 2, 3}
o = {"a", "b", "c"}
u.update(o)
u.update(["Karim", "C++"])
u.update((True, False))

print(u)


print("*" * 50)


# difference()

s1 = {1, 2, 3, 4}
s2 = {1, 2, "Karim", "Tantawy"}

print(s1)
print(s1.difference(s2))  # s1 - s2
print(s1)


print("*" * 50)


# difference_update()

s3 = {1, 2, 3, 4}
s4 = {1, 2, "Karim", "Tantawy"}

print(s3)
s3.difference_update(s4)
print(s3)


print("*" * 50)


# intersection()

s5 = {1, 2, 3, 4, "Yes"}
s6 = {"Karim", "No", "Yes", 1}

print(s5)
print(s5.intersection(s6))  # s5 ∩ s6
print(s5)


print("*" * 50)


# intersection_update()

s7 = {1, 2, 3, 4, "Yes"}
s8 = {"Karim", "No", "Yes", 1}

print(s7)
s7.intersection_update(s8)  # s5 ∩ s6
print(s7)


print("*" * 50)


# symmetric_difference()

s9 = {1, 2, 3, 4, "X"}
s10 = {"Karim", "Tantawy", True, "X", 2}

print(s9)
print(s9.symmetric_difference(s10))
print(s9)


print("*" * 50)


# symmetric_difference_update()

s11 = {1, 2, 3, 4, "X"}
s12 = {"Karim", "Tantawy", True, "X", 2}

print(s11)
s11.symmetric_difference_update(s12)
print(s11)


print("*" * 50)


# issuperset()

s13 = {1, 2, 3, 4}
s14 = {1, 2, 3}
s15 = {1, 2, 3, 4, 5}
print(s13.issuperset(s14))  # True
print(s13.issuperset(s15))  # False


print("*" * 50)


# issupset()    # Opposite to issuperset()

print(s13.issubset(s14))  # False
print(s13.issubset(s15))  # True


print("*" * 50)


# isdisjoint()

s16 = {1, 2, 3, 4}
s17 = {1, 2, 3}
s18 = {10, 20, 30}

print(s16.isdisjoint(s17))  # False  => There are common elements between the two
print(s16.isdisjoint(s18))  # True   => There ain't common elements between the two
