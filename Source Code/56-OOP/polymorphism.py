class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def __add__(self, other):
        return self.__age + other.__age
    
    def __str__(self):
        return f"Name: {self.__name}\nAge: {self.__age}"
    
    
person1 = Person("Karim", 23)
person2 = Person("Omar", 22)

print(person1)
print(person2)

person1.__age = person1.__add__(person2)

combined_age = person1 + person2

print(f"Combined age is: {combined_age}")



class Member:
    def __init__(self, name):
        self.__name = name
       
    @property 
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def set_name(self, name):
        self.__name = name
    
    def __del__(self):
        print(f"'{self.__name}' from Member class has been deleted!")
    
member1 = Member("Karim")
member2 = Member("Ibrahim")
member3 = Member("Yousef")

member1.__name = "Mohamed"

print(member1.get_name)  # Karim

print(member1.__name)  # Mohamed  =>  doesn't affect the class attribute

member1._Member__name = "Islam"   # This affects the class attribute by removing the security layer


print(member1.get_name)   # Islam

print(member2.get_name)   # Ibrahim

member2.set_name = "Ahmed"

print(member2.get_name)   # Ahmed

print(member3.get_name)   # Yousef

member3.set_name = "Yousef Ahmed"

print(member3.get_name)   # Yousef Ahmed


print("*"*50)

