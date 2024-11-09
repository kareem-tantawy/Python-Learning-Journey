# --------------------- #
# -- Basic Calculate -- #
# --------------------- #

# Program Starts
print('='*40)
print(" Basic Calculator App ".center(40))
print('='*40)

# Collecting Data
firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the first number: "))
operation = input(f"Enter the operation between '{firstNum}' and '{secondNum}'\n\
1- '+'\n2- '-'\n3- '*'\n4- '/'\n5- '%'\nOperation: ")

# Solver!
if operation == '1' or operation == '+':
    print(f"The Summation = {firstNum + secondNum}")
elif operation == '2' or operation == '-':
    print(f"The Subtraction = {firstNum - secondNum}")
elif operation == '3' or operation == '*':
    print(f"The Multiplication = {firstNum * secondNum}")
elif operation == '4' or operation == '/':
    print(f"The Division = {firstNum / secondNum}")
elif operation == '5' or operation == '%':
    print(f"The Modulus = {firstNum % secondNum}")
else:
    print("Please enter a valid input!\nYou Can enter either the number of the operation\
or the operation it self")
    
print('='*40)    
print("Thank You For Using Our App".center(40))
print('='*40)    
