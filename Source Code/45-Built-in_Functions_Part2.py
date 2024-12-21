# ------------------------------- #
# -- Built In Functions => Map -- #
# ------------------------------- #
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function


def formatText(text):
    return f"- {text.strip().capitalize()} -"


myName = ["  Karim", "  Ahmed ", "Tantawy"]

formatedText = map(formatText, myName)


for name in formatedText:
    print(name)


print("*" * 20)

for name in list(map(formatText, myName)):
    print(name)


print("*" * 20)

# Use Map With lambda function

for name in list(map(lambda text: f"# {text.strip().capitalize()}", myName)):
    print(name)

print("*" * 40)

# ---------------------------------- #
# -- Built In Functions => Filter -- #
# ---------------------------------- #
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example


def checkNum(num):
    return num if num > 10 else None


myNumbers = [15, 3, 167, 31, 487, 21, 56, 1, 4, 43, 9]
Result = filter(checkNum, myNumbers)

for num in filter(checkNum, myNumbers):
    print(num)

print("*" * 10)


def checkZero(num):
    return True if num == 0 else None  # if we wrote return num it won't return nothing


zeros = [0, 0, 0]


for num in filter(checkZero, zeros):
    print(num)

print("*" * 10)


def checkName(name):
    return name.startswith("K")


names = ["Ahemd", "Kimo", "Tantawy", "Karim", "Tarek"]

for na in filter(checkName, names):
    print(na)


print("*" * 10)


for name in filter(lambda name: name.startswith("T"), names):
    print(name)

print("*" * 30)

# ---------------------------------- #
# -- Built In Functions => Reduce -- #
# ---------------------------------- #
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# [3] Then Run Function On Result And Third Element
# ----------------------------------------------------------------------

from functools import reduce


def Reduce(num1, num2):
    return num1, num2


def sumNumbers(num1, num2):
    return num1 + num2


numbers = [1, 2, 4, 8, 16, 64]

print(reduce(Reduce, numbers))  # shows the workflow of reduce()

print("*" * 10)

result = reduce(sumNumbers, numbers)
print(result)


print("*" * 10)

print("From Lambda!", end="\n\n")
print(reduce(lambda num1, num2: num1 + num2, numbers))
