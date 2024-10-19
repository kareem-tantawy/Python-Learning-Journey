# This code represent the formating of strings in Python

#*******************************************************************#
                # ---------------------------------#
                # -- Strings Formatting Old Ways --#
                # ---------------------------------#                
#*******************************************************************#

name = "Karim"
age = 23
Percentage = 85.74

print("My name is " + name)
# print("My name is " + name + " and My age is " + age)  # Error

print("My name is %s" % "Karim")
print("My name is %s" % name)
print("My name is %s and my age is %d" % (name, age))
print("My name is %s and my age is %d, and I got %f as a total grade" % (name, age, Percentage))  # Same as the upove one but we use %d for numbers

# To control Floating point numbers
print("My name is %s and my age is %d, and I got %f as a total grade" % (name, age, Percentage))

# Use %.anyNumber+f to specify the numbers after the decimal point


# %s  =>  String
# %d  =>  Integer
# %f  =>  Float


n = "Karim"
l = "Python"
y = 2

print("My name is %s, I'm a Python developer %s with %s years of EXP" % (n,l,y))



#Truncate
msg = "My name is Karim"
print("Message: %.4s" % msg)


#*******************************************************************#
                # ---------------------------------#
                # -- Strings Formatting New Ways --#
                # ---------------------------------#                
#*******************************************************************#

print("My name is {:s}".format("Karim"))
print("My name is {:s}".format(name))
print("My name is {:s} and my age is {:d}".format(name, age))
print("My name is {:s} and my age is {:d}, and I got {:f} as a total grade".format(name, age, Percentage))  # Same as the upove one but we use %d for numbers

# To control Floating point numbers
print("My name is {:s} and my age is {:d}, and I got {:.2f} as a total grade".format(name, age, Percentage))



# {:s}  =>  String
# {:d}  =>  Integer
# {:f}  =>  Float


n = "Karim"
l = "Python"
y = 2

print("My name is {:s}, I'm a Python developer {:s} with {:d} years of EXP".format(n,l,y))


#Truncate
msg = "My name is Karim"
print("Message: {:.3s}".format(msg))




# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
print("My Money in Bank Is: {:_d}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney))


# Rearranging Items

a, b, c = "One", "Two", "Three"
print("Hello, {1:s}, {0:s}, {2:s}".format(a, b, c))


# Format in Version 3.6+

myName = "Kareem"
myAge = 23

print("My name is {myName}, And my age is {myAge}")
print(f"My name is {myName}, And my age is {myAge}")