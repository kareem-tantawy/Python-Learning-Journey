# ----------------- #
# -- Loop => For -- #
# --  Trainings  -- #
# ----------------- #


# Range

myRange = range(1, 101)

for num in myRange:
    print(num)

MyRange = range(2,10,2)  # 2 4 6 8

for num in MyRange:
    print(num)


# Dictionary

mySkills = {
    "C++" : "90%",
    "Python" : "70%",
    "Css" : "5%",
    "Html" : "2%",
    "JavaScript" : "0%"
}

print(mySkills["Python"])
print(mySkills.get('C++'))

for skill in mySkills:  
    print(f"My progress in languge {skill} is: {mySkills.get(skill)}")
