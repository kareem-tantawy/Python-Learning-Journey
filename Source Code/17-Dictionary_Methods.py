# ------------------------ #
# -- Dictionary Methods -- #
# ------------------------ #

# clear()

user = {
    "name" : "Karim",
    "age" : 23
}

print(user)
user.clear()
print(user)


print('*' * 50)


# update()

member1 = {
    "name" : "Karim"
}

member1["age"] = 23
print(member1)

member1.update({"tall" : 168.5})
print(member1)


print('*' * 50)


# copy()

member2 = member1.copy()
print(member2)


print('*' * 50)


# setdefault()

member3 = {
    "name" : "Karim"
}

print(member3)
print(member3.setdefault("age", 23))
print(member3)


print('*' * 50)


# popitem()

member4 = {
    "name" : "Karim",
    "age" : 23
}

print(member4.popitem())


print('*' * 50)


# items()

member5 = {
    "name" : "Ahmed",
    "age" : 57
}

members = member5.items()

print(member5)
member5.update({"hobby" : "reading"})
print(member5)
print(members)


print('*' * 50)


# fromkeys()

a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
b = 'x'

print(dict.fromkeys(a,b))