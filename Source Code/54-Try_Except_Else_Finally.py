"""
# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------
"""

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Only interger values are allowed!")

except:
    raise NotImplementedError(
        "Some Error accured when inputing data, try to enter positive interger"
    )

else:
    print("Thank you for entering you age")

finally:
    print("Thank you for using our app")
