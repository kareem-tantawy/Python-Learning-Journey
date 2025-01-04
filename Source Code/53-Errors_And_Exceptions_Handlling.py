# ----------------------------------- #
# -- Errors And Exceptions Raising -- #
# ----------------------------------- #
"""
# -----------------------------------------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------
"""


def divid_numbers(n1,n2):
    if n2 == 0:
        raise ZeroDivisionError("You can't divid by zero!")
    return n1/n2

age = int(input("Enter your age: "))

if age > 18:
    print("Access Granted!")
else:
    raise NotImplementedError("Access Denied!")

print("Checks whether the exception is actually working or not")
