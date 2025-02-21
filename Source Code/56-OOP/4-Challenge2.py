"""
   ** بسم الله الرحمن الرحيم **
"""


class User:
    def __init__(self, first_name, last_name, email, password, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email Name: {self.email}")
        print(f"Status Name: {self.status}")


def create_user():
    try:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
    except ValueError as ve:
        print(f"Error: {ve} try again!")
    else:
        print("User added successfully!")
        return User(first_name, last_name, email, password)


print("Welcom to user management system")
users = []

while True:
    print()
    print("1. Add new user")
    print("2. Display all users")
    print("3. Exit\n")
    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                users.append(create_user())
            case 2:
                if len(users) == 0:
                    print("You haven't added any users yet, press 1 to add on")
                print("Displaying all users ....")
                for i in range(len(users)):
                    print("*" * 30)
                    users[i].display_info()
                    print("*" * 30)
            case 3:
                print("Exiting...")
                break
    except TypeError as te:
        print("Error: Please enter a valid input")
        break
    except ValueError as ve:
        print(f"Error: {ve}, please try again")
