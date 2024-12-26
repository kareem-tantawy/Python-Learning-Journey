# ----------------------------------------- #
# -- Modules => Creating Private Modules -- #
# ----------------------------------------- #

import sys

sys.path.append(r"E:\Programming\Python-Learning-Journey\testing_file")

import Karim

# print(dir(Karim))

Karim.sayHello("Karim")
Karim.sayHello("Tantawy")

print(Karim.sum(10, 5))

import Karim as KT

KT.sayHello("Karim Tantawy")
print(KT.sum(20, 30))


from Karim import sayHello as SH

SH("Ahmed")
