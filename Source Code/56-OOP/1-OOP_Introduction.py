# pylint: disable=invalid-name


import datetime

class Car:
    """
    Represents a car with its name, model year, color, and maximum speed.
    """

    def __init__(self, name: str, model: int, color: str, max_speed: int) -> None:
        """
        Initializes a Car object.

        Args:
            name (str): The name of the car.
            model (int): The model year of the car.
            color (str): The color of the car.
            max_speed (int): The maximum speed of the car (in km/h).
        """

        self.name = name
        self.model = model
        self.color = color
        self.max_speed = max_speed

    def show_details(self) -> None:
        """
        Prints the details of the Car object.
        """

        print(f"Car name: {self.name}")
        print(f"Car model: {self.model}")
        print(f"Car color: {self.color}")
        print(
            f"Max speed of {self.name} car is: {self.max_speed} km/h"
        )  # Clarify units


# Improved error handling with specific exception and informative message
try:
    car_1 = Car("Jeep", 2025, "Black", 350)
    car_1.show_details()
except ValueError as e:  # More specific for invalid types
    print(f"Invalid value provided: {e}")
except TypeError as e:  # Handle missing arguments
    print(f"Missing required arguments: {e}")

print("*" * 30)

car_2 = Car("BMW", 2023, "Blue", 425)
car_2.show_details()

print("*" * 50)
print("*" * 50)


class Person:
    """
    Represents a person with their name, gender, age, and height.
    """

    def __init__(self, name: str, gender: str, age: int, height_cm: int) -> None:
        """
        Initializes a Person object.

        Args:
            name (str): The name of the person.
            gender (str): The gender of the person.
            age (int): The age of the person.
            height_cm (int): The height of the person in centimeters.
        """

        self.name = name
        self.gender = gender
        self.age = age
        self.height_cm = height_cm  # Use appropriate attribute name

    def get_details(self) -> str:
        """
        Returns a formatted string containing the person's details.
        """

        return (
            f"General Detail on {self.name}!\n"
            f"His gender is: {self.gender}\n"
            f"His age is: {self.age}\n"
            f"His height is: {self.height_cm} cm"
        )


person1 = Person("Karim", "Male", 23, 168)
print(person1.get_details())

print("*" * 50)
print("*" * 50)


class Book:
    """
    Represents a book with its title, author, and number of pages.
    """

    def __init__(self, title: str, author: str, pages: int) -> None:
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            pages (int): The number of pages in the book.
        """

        self.title = title
        self.author = author
        self.pages = pages

    def show_details(self) -> None:
        """
        Prints the details of the Book object.
        """

        print(f"General notes on '{self.title}' book!")
        print(f"The author of the book is: '{self.author}'")
        print(f"The number of pages in this book is: {self.pages}")


my_book = Book("Origin", "Dan Brown", 542)
my_book.show_details

"""Module containing the Member class."""


class human:
    def __init__(self, name, date_of_birth, id, gender, email, passwrod):
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__id = id
        self.__gender = gender
        self.__email = email
        self.__password = passwrod
        
    def get_name(self):
        return self.__name
    
    def get_date_of_birth(self):
        return self.__date_of_birth.strftime("%d/%m/%Y")

    def get_id(self):
        return self.__id
    
    def get_gender(self):
        return self.__gender
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    
    def set_name(self, new_name):
        self.__name = new_name
        
    def set_id(self, new_id):
        self.__id = new_id
        
    def set_email(self, new_email):
        self.__email = new_email
    
    def set_password(self, new_password):
        self.__password = new_password

    def display_info(self):
        print(f"name: {self.__name}")
        print(f"ID: {self.__id}")
        print(f"Date of birth: {self.__date_of_birth.strftime("%d/%m/%Y")}")
        print(f"gender: {self.__gender}")
        print(f"Email: {self.__email}")

    def get_age(self):
        return datetime.date.today().year - self.__date_of_birth.year
    
    












class Member:
    """
    Represents a member with a first name, last name, and gender.
    """

    def __init__(self, first_name: str, last_name: str, gender: str) -> None:
        """
        Initializes a Member object.

        Args:
            first_name (str): The first name of the member.
            last_name (str): The last name of the member.
            gender (str): The gender of the member (e.g., "male", "female").
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender.lower()  # Normalize gender input

    def get_full_name(self) -> str:
        """
        Returns the full name of the member.

        Returns:
            str: The full name (first name + last name).
        """
        return f"{self.__first_name} {self.__last_name}"

    def greeting(self) -> str:
        """
        Returns a gender-specific greeting.

        Returns:
            str: A greeting string (e.g., "Hello mr Karim", "Hello miss Karim").
            Returns a generic greeting if gender is not recognized.
        """
        if self.__gender == "male":
            return f"Hello mr {self.__first_name}"
        elif self.__gender == "female":  # Explicitly check for "female"
            return f"Hello miss {self.__first_name}"
        else:
            return f"Hello {self.__first_name}"  # Default greeting

    def all_details(self) -> str:
        """
        Returns all details of the member, including the greeting and full name.

        Returns:
            str: A string containing the greeting and full name.
        """
        return f"{self.greeting()}\nYour full name is {self.get_full_name()}"


def main():
    """
    Main function to demonstrate the Member class.
    """
    member1 = Member("Karim", "Tantawy", "Male")  # Test with capitalized gender
    print(member1.greeting())
    print(member1.get_full_name())
    print(member1.all_details())

    member2 = Member("Sarah", "Smith", "female")
    print(member2.greeting())

    member3 = Member("Alex", "Lee", "Other")  # Test with other gender
    print(member3.greeting())


if __name__ == "__main__":
    main()
