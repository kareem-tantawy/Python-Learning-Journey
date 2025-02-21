"""
بسم الله الرحمن الرحيم
"""


class Recipe:
    def __init__(self, name, ingredients, time, instructions):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.instructions = instructions

    def display_recipe(self):
        print("Displaing recipe ....")
        print(f"Name: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Cooking Time: {self.time}")
        print(f"Instructions: {self.instructions}")


def create_recipe():
    name = input("Entre recipe name: ")
    ingredients = input("Entre Ingredients: ")
    time = input("Entre cooking time: ")
    instructions = input("Entre cooking instructions: ")
    print("Recipe added successfully!\n")

    return Recipe(name, ingredients, time, instructions)


print("Welcome to Recipe Collection\n")

recipe1 = create_recipe()
recipe1.display_recipe()
