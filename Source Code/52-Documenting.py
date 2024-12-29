# -------------------------------------------- #
# -- Doc String & Commenting vs Documenting -- #
# -------------------------------------------- #
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------


def Karim_function(name):
    """
    Karim Function
      It Say Hello From Karim
    Parameter:
      name => Person Name That Use Function
    Return:
      Return Hello Message To The Person
    """
    print(f"Hello {name} From Karim")


Karim_function("Tantawy")

print(dir(Karim_function))

print(Karim_function.__doc__)

help(Karim_function)
