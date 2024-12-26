# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import main module

import random

# print(random)

print("Show all functions in 'random' module\n", dir(random))

from random import randint, randrange

print(f"Printing random integer {randint(-10,10)}")


print('*'*50)

# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------


import termcolor
import pyfiglet

# print(dir(pyfiglet))

# print(pyfiglet.figlet_format("Karim"))

print(termcolor.colored(pyfiglet.figlet_format("Karim"), color="yellow"))