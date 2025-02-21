class Father:
    def __init__(self, name):
        self.name = name
        
    def get_gender(self):
        return "Male"
    

class Mother:
    def __init__(self, name):
        self.name = name
        
    def get_gender(self):
        return "Female"
    
class Son(Father):
    pass

class Daughter(Mother):
    pass

son1 = Son("Islam")
print(son1.get_gender())

daughter1 = Daughter("Roqia")
print(daughter1.get_gender()) 


print('*'*30)


class Thing:
    def __init__(self, type, color):
        self._type = type
        self._color = color
    
    def get_type(self):
        return self._type
    def get_color(self):
        return self._color
    

class Chair(Thing):
    def __init__(self, color):
        Thing.__init__(self, type, color)
        self._type = "Chair"
        self.color = color
        
    def get_color(self):
        return self.get_color

class Person(Thing):
    def __init__(self, gender, color):
        super().__init__(type, color)
        self._type = gender
        
        
chair1 = Chair("White")
print(chair1.get_type())
print(chair1.get_color())


person1 = Person("Male", "white")

print(person1.get_type())
print(person1._type)



print('*'*30)



class Human(Person):
    def __init__(self, name, gender, color, age):
        super().__init__(gender, color)
        self.name = name
        self.age = age
        
    def get_info(self):
        print("Human Info...")
        print(f"Name: {self.name}")
        # print(f"Color: {self.color}")
        print(f"Color from Person(Thing): {self._color}")
        print(f"Gender: {self._type}")
        print(f"Age: {self.age}")


me = Human("Karim", "Male", "White", 23)

me.get_info()



print('*'*30)



class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("General animal sound")
        
    def __del__(self):
        print(f"{self.name} has been removed!")
        
        
class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.sound}")
        
        
cat = Animal("Kitty")
dog = Dog("Jack", "Woof!")

cat.make_sound()
dog.make_sound()



print("*"*30)



class Shape:
    def calculate_area(self, base, height):
        return base * height
    
    
class Rectangle(Shape):
    def calculate_area(self, base, height):
        return base * height            