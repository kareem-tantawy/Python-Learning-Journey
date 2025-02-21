import re

VALIDATE_EMAIL = r"^([A-z0-9._%+-]+)@([A-z0-9._%+-]+)\.([A-z]{2,})$"


class Profile:
    def __init__(self, username: str, email: str, language: str):
        try:
            self.username = username
            self.language = language
            self.email = email
            if re.search(VALIDATE_EMAIL, email):
                pass
            else:
                raise ValueError("Email is not valid!")

        except ValueError as ve:
            print(f"{ve}: Input is not valid!")
        except TypeError as te:
            print(f"{te}: Type is not valid!")

    def show_data(self):
        print(f"--> {self.username} <--")
        print(f"--> {self.email} <--")
        print(f"--> {self.language} <--")


student1 = Profile("Kairm", "karim@yahoo.com", "English")

student1.show_data()


print("*" * 50)


from datetime import datetime


class Message:
    def __init__(self, sender, receiver, msg_body, msg_date):
        self.sender = sender
        self.receiver = receiver
        self.msg_body = msg_body
        self.msg_date = msg_date

    def display_message_info(self):
        print("== Message info ==")
        print(f"Sent by: {self.sender}")
        print(f"received by: {self.receiver}")
        print(f"Message Content\n{self.msg_body}")
        print(f"Date: {self.msg_date}")


msg1 = Message(
    "Karim", "Mohamed", "How are you Mohamed\nWe missed you so much", datetime.now()
)
msg1.display_message_info()


class Product:
    def __init__(self, title, price, description, rate):
        self.title = title
        self.price = price
        self.description = description
        self.rate = rate

    def update_title(self, new_title):
        self.title = new_title

    def update_price(self, new_price):
        self.price = new_price

    def update_description(self, new_description):
        self.description = new_description

    def update_rate(self, new_rate):
        self.rate = new_rate

    def show_details(self):
        print("*" * (max(len(self.title), len(self.description)) + 15))
        print("Title", "->".rjust(8), self.title)
        print("Price", "->".rjust(8), self.price)
        print("Description", "->".rjust(1), self.description)
        print("Rate", "->".rjust(9), self.rate)
        print("*" * (max(len(self.title), len(self.description)) + 15))


toy = Product("Car", 10, "Car toy", 7.8)

toy.update_price(15)

toy.show_details()


class Task:
    def __init__(
        self,
        title,
        description,
        priority="Medium",
        status="To-Do",
        due_date=datetime.now(),
    ):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date

    def update_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status

    def get_priority(self):
        return self.priority

    def get_due_date(self):
        return self.due_date

    def get_description(self):
        return self.description

    def show_details(self):
        print("*" * (max(len(self.title), len(self.description)) + 15))
        print("Title", "->".rjust(8), self.title)
        print("Description", "->".rjust(1), self.description)
        print("Priority", "->".rjust(5), self.priority)
        print("Status", "->".rjust(7), self.status)
        print("Due Date", "->".rjust(5), self.due_date)
        print("*" * (max(len(self.title), len(self.description)) + 15))


task1 = Task("Study Python", "Study Python for 1 hour", "High", "To-Do", datetime.now())
task1.show_details()

task1.update_status("Done")
task1.show_details()
