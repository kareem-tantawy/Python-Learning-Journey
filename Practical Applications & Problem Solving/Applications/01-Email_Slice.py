# -------------------------- #
# -- Practical Slice Email --#
# -------------------------- #

uName = input("Enter your name: ").strip().capitalize()
uEmail = input("Enter your email: ").strip().lower()

username = uEmail[:uEmail.index('@')]
domain = uEmail[uEmail.index('@')+1 :]

print(f"Hello {uName}, your email is: {uEmail}")
print(f"Your username is: {username}")
print(f"Your domain is: {domain}")
