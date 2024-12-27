# ------------------------ #
# -- Age Calculator App -- #
# ------------------------ #

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Open the birthdays file in append mode to record user details
birthdays_ = open(
    r"E:\Programming\Python-Learning-Journey\testing_file\Birhtdays.txt", "a"
)

# Prompt the user for their name
uName = input("Please Enter Your Name: ")

# Write the user's name to the file
birthdays_.write(f"{uName}: ")

# Greet the user and ask for their birthday
print(f"Hello Mr./Ms. {uName}, Nice to meet you!")
print("Can you tell me what your birthday is?")
print("Please write it in this format: day/month/year")

# Read and parse the birthday input from the user
Day, Month, Year = map(int, input("Input: ").split("/"))

# Create a datetime object for the user's birthday
birthday = datetime(Year, Month, Day)

# Write the user's birthday to the file
birthdays_.write(f"{birthday.strftime("%d/%m/%Y")}\n")

# Prompt user to proceed with age calculations
input("Are you ready to see your age in different units? Press Enter to continue...")

# Calculate the precise age using relativedelta
age = relativedelta(datetime.now(), birthday)

# Calculate total days, hours, minutes, and seconds lived
age_in_days = (datetime.now() - birthday).days
age_in_hours = age_in_days * 24
age_in_minutes = age_in_hours * 60
age_in_seconds = age_in_minutes * 60

# Calculating the next birthday
if datetime.now().month > birthday.month:
    next_birthday = datetime(datetime.now().year + 1, Month, Day)
else:
    next_birthday = datetime(datetime.now().year, Month, Day)
next_birthday_ = relativedelta(next_birthday, datetime.now())


print(next_birthday)


# Printing a border to show the data more clearly
print("\n", "*" * 25, sep="")

# Printing the weekday in which the user was born on
print(f"You were born on {birthday.strftime("%A")}")

# Printing the age in different units
print("\nYou have lived for:")
print(f"  {age.years} years")
print(f"  {age.months} months")
print(f"  {age.days} days")
print(f"  {age_in_days} total days")
print(f"  {age_in_hours} total hours")
print(f"  {age_in_minutes} total minutes")
print(f"  {age_in_seconds} total seconds")

# Printing the next birthday information
print("\nYour next birthday will be after:")
print(f"  {next_birthday_.months} months & {next_birthday_.days + 1} days")

# Printing a border to show the data more clearly
print("*" * 25)

# Write a separator line to the file for better readability
separator_length = len(uName) + 12
birthdays_.write("=" * separator_length + "\n")

# Close the file after writing
birthdays_.close()
