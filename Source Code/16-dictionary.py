# ---------------- #
# -- Dictionary -- #
# ---------------- #
# ------------------------------------------------------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple)
#     List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ------------------------------------------------------------

# Dictionary

user = {
    "name": "Karim",
    "age": 23,
    "country": "Egypt",
    "Skills": ["C++", "Python"],
    "name": "Tantawy",
}

print(user)
print(user.get("name"))  # => updated name to 'Tantawy'
print(user["age"])  # 23

print(user.keys())
print(user.values())


# Two-Dimensional Dictionary

languages = {
    "One": {
        "name": "C++",
        "progress": "89%",
        "rate": 9.8
            },
    "Two": {
        "name": "Python",
        "progress": "45%",
        "rate": 9.9
            },
}

print(languages["Two"]["name"])


# Dictionary length

print(len(languages))
print(len(languages["One"]))


# Create Dictionary form variables

frameworkOne = {
    "name": "Vuejs",
    "progress": "80%"
    }

frameworkTwo = {
    "name": "ReactJs",
    "progress": "80%"
                }

frameworkThree = {
    "name": "Angular",
    "progress": "80%"
                  }

allFramework = {
    "one": frameworkOne,
    "two": frameworkTwo,
    "three": frameworkThree
    }

print(allFramework)
