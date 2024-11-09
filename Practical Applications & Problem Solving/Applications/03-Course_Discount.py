# --------------------------- #
# --  Course Discount App  -- #
# --------------------------- #

userName = input("username: ")
userCountry = input("Country: ").strip().capitalize()
password = input("Password: ")
   
isStudent = input("Are you Sturdent? (y/n) ")
if isStudent == 'y':
    isStudent = True
else:
    isStudent = False

print("="*20)
print(f"Access successful!\nWelcome {userName}!")
print("="*20)
print("\nSelect the course you want to but...\n'1-Python Course'\n'2-C++ Course'\n'3-HTML Course'")

courseName = int(input('Enter the number of the course: '))
coursePrice = 0

if courseName == 1:
    courseName = "Python"
    coursePrice = 120
elif courseName == 2:
    courseName = "C++"
    coursePrice = 200
else:
    courseName = "HTML"
    coursePrice = 70

courseDiscount = 0

if userCountry == "Egypt":
    courseDiscount = .9
    if isStudent:
        courseDiscount = 1
elif userCountry == "Saudi":
    courseDiscount = .5
    if isStudent:
        courseDiscount = .9
elif userCountry == "Emarat":
    courseDiscount = .3
    if isStudent:
        courseDiscount = .8
else:
    courseDiscount = .15
    if isStudent:
        courseDiscount = .5
    
print(f"Thank for choosing '{courseName}' Course\n\
Course Price: ${coursePrice}\nGood news {userName} ^_^\n")
print(f"Because you're from '{userCountry}', and you're a 'Student'" if isStudent
else f"Because you're from '{userCountry}'")    
print(f"You got {int(courseDiscount*100)}% off ( $ _ $ )\n\
Final Price: ${(coursePrice * (1-courseDiscount)):.2f}")
    