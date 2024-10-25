# ------------- #
# -- Numbers -- #
# ------------- #


# Integers

print(type(1))
print(type(0))
print(type(-10))


# Float

print(type(1.2))
print(type(-0.7))


# Complex

print(type(3 + 5j))

comp = 3 + 7.5j

print(type(comp))
print("Real part is: {:d}\nImaginary part is: {:.2f}".format(int(comp.real), comp.imag))
print(f"Real part is: {int(comp.real)}")
print(f"Imaginary part is: {comp.imag}")

comp2 = -1 -2j

print(comp2*comp)