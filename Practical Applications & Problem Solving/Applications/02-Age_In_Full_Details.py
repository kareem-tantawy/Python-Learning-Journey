# ----------------------------------- #
# -- Practical Age In Full Details -- #
# ----------------------------------- #

age = int(input("Enter your age: "))


# Get age in all time units
months = age*12
weeks = age*52
days = age*365
hours = days*24
minuts = hours*60
seconds = minuts*60
print(f"Your age in months: {months:,}")
print(f"Your age in weeks: {weeks:,}")
print(f"Your age in days: {days:,}")
print(f"Your age in hours: {hours:,}")
print(f"Your age in minuts: {minuts:,}")
print(f"Your age in seconds: {seconds:,}")