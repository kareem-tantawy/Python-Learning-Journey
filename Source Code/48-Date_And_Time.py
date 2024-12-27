# ----------------------------------- #
# -- Date and Time => Introduction -- #
# ----------------------------------- #

import datetime


# print the current data & time
print(datetime.datetime.now())

print("*" * 40)


# print the current year
print(datetime.datetime.now().year)

print("*" * 40)


# print the current month
print(datetime.datetime.now().month)

print("*" * 40)

# print the current day
print(datetime.datetime.now().day)

print("*" * 40)


# print start & end of date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("*" * 40)


# print the current time
print(datetime.datetime.now().time())

print("*" * 40)


# print the current hour
print(datetime.datetime.now().time().hour)

print("*" * 40)


# print the current minute
print(datetime.datetime.now().time().minute)

print("*" * 40)


# print the current second
print(datetime.datetime.now().time().second)

print("*" * 40)

# print the min & max of time
print(datetime.time.min)
print(datetime.time.max)

print("*" * 40)


# print specific date
print(datetime.datetime(2001, 6, 28))
print(datetime.datetime(2001, 6, 28, 22, 30, 7))


print("*" * 40)

# Formating date & time
myBirthday = datetime.datetime(2001, 6, 28)

print(myBirthday)
print(myBirthday.strftime("%a-%d-%b"))
