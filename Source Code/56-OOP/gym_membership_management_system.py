"""
   ** بسم الله الرحمن الرحيم **
   Gym Management System
"""

import os
import time


def clear_terminal():
    """Function to clear the terminal for better user input experience"""
    os.system("cls" if os.name == "nt" else "clear")


"""
# This was a suggestion method to generate ID for members using generators but we prefered to use class attributes to do it

def generate_id():
    """ """Generator function to generate unique incremental IDs.""" """
    counter = 1  # Initialize the counter within the generator
    while True:  # Create an infinite loop
        yield counter  # Return the current counter value and pause execution
        counter += 1  # Increment the counter for the next call

id_generator = generate_id()  # Create an instance of the generator

"""


class Member:
    """Class to represent a club member."""

    current_id = 1

    def __init__(self, first_name: str, last_name: str, subscription_fees: int):
        """basic constructor for the class"""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__subscription_fees = subscription_fees
        self.__id = Member.current_id
        self.__status = "active"
        Member.current_id += 1

    def get_first_name(self):
        """getter for first name"""
        return self.__first_name

    def get_last_name(self):
        """getter for last name"""
        return self.__last_name

    def get_id(self):
        """getter for id"""
        return self.__id

    def get_status(self):
        """getter for status"""
        return self.__status

    @classmethod
    def get_no_of_members(cls):
        return Member.current_id

    def display_info(self):
        """Displays information about the member."""
        print(f"First Name: {self.__first_name}")
        print(f"Last Name: {self.__last_name}")
        print(f"Membership Plan: {self.__subscription_fees}$")
        print(f"Membership ID: {str(self.__id).zfill(3)}")
        print(f"Status: {self.__status}")

    def update_status(self, new_status: str):
        """Updates the status of the member."""
        self.__status = new_status

    def update_name(self, f_name: str, l_name: str):
        """Updates the name of the member."""
        self.__first_name = f_name
        self.__last_name = l_name

    def update_subscription(self, new_subscription):
        """setter for updating member status"""
        self.__subscription_fees = new_subscription

    @staticmethod
    def search(members: list, criterion: str, value):
        """Searches for members based on the specified criterion."""
        result = []
        for member in members:
            if criterion == "id" and member.__id == value:
                return [member]
            elif criterion == "name" and (
                value in {member.__first_name, member.__last_name}
            ):
                result.append(member)
            elif criterion == "status" and member.__status == value:
                result.append(member)
        return result


def display_subscription_plans():
    """Displays available subscription plans."""
    plans = {1: 10, 2: 100, 3: 250}
    print("\nChoose one of our plans:")
    for key, value in plans.items():
        print(f"{key}. Plan costs {value}$")
    return plans


def get_valid_choice(prompt, valid_choices):
    """Ensures a valid choice is entered."""
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            print(f"Invalid choice. Valid options: {valid_choices} not including end")
        except ValueError:
            print("Please enter a valid number.")


def create_member():
    """Creates a new member."""
    clear_terminal()
    try:
        first_name = input("Enter first name: ").capitalize().strip()
        last_name = input("Enter last name: ").capitalize().strip()
        plans = display_subscription_plans()
        subscription = get_valid_choice("\nEnter subscription plan: ", plans.keys())
        subscription_fees = plans[subscription]
        print("Member added successfully!")
        return Member(first_name, last_name, subscription_fees)
    except Exception as e:
        print(f"An error occurred while creating a member: {e}")
        return None


def search_member(members_list):
    """The main function for searching for a member"""
    clear_terminal()
    print("Choose one of search methods below\n")
    print("1. Search by name")
    print("2. Search by Id")
    print("3. Search by status")
    print("4. Return to the main menu")
    search_method = get_valid_choice("\nEnter search method: ", range(1, 5))

    try:
        match search_method:
            case 1:
                name_tracked = (
                    input("Enter the first or the last name of the member: ")
                    .capitalize()
                    .strip()
                )
                return Member.search(members_list, "name", name_tracked)
            case 2:
                id_tracked = int(input("Enter member Id: "))
                return Member.search(members_list, "id", id_tracked)
            case 3:
                status_tracked = input("Enter status: ")
                return Member.search(members_list, "status", status_tracked)
            case 4:
                return 4
    except ValueError:
        print("Invalid input. Please try again.")
    return []


def dashboard():
    """Displays the dashboard for member management."""
    clear_terminal()
    print("-" * 19)
    print(" Members Dashboard")
    print("-" * 19, "\n")
    print("1. Add new member")
    print("2. Change member status")
    print("3. Change member name")
    print("4. Change member subscription")
    print("5. Delete member")
    print("6. Display the number of members")
    print("7. Return to the main menu")
    return get_valid_choice("\nEnter your choice: ", range(1, 8))


def manage_members(members_list):
    """Manages member updates and deletions."""
    while True:
        clear_terminal()
        member_choice = dashboard()

        if member_choice == 1:
            member = create_member()
            if member:
                members_list.append(member)
                members_list[-1].display_info()
                time.sleep(2)
        elif member_choice in {2, 3, 4, 5}:
            search_results = search_member(members_list)
            if search_results == 4:
                continue
            if not search_results:
                print("No matching members found.")
                continue
            if member_choice == 2:
                new_status = input("Enter the new status: ").strip()
                for member in search_results:
                    member.update_status(new_status)

            elif member_choice == 3:
                new_first_name = input("Enter new first name: ").capitalize().strip()
                new_last_name = input("Enter new last name: ").capitalize().strip()
                for member in search_results:
                    member.update_name(new_first_name, new_last_name)

            elif member_choice == 4:
                plans = display_subscription_plans()
                subscription = get_valid_choice(
                    "\nEnter new subscription plan: ", plans.keys()
                )
                new_subscription = plans[subscription]
                for member in search_results:
                    member.update_subscription(new_subscription)

            elif member_choice == 5:
                for member in search_results:
                    if member in members_list:
                        members_list.remove(member)
                        print(f"Member ID {member.get_id()} has been removed.")
                        time.sleep(1)

        elif member_choice == 6:
            print(f"The number of members are: {Member.current_id-1}")
            while True:
                flag = input(f"Do you want to display them? (y/n): ")
                if flag == "y" or flag == "Y":
                    print("Displaying all members:\n" + "*" * 30)
                    for member in members_list:
                        member.display_info()
                        print("-" * 30)
                        time.sleep(0.5)
                    break
                elif flag == "n" or flag == "N":
                    break
                else:
                    print("Invalid input, please enter a valid input")
                    continue

        elif member_choice == 7:
            break


def main_menu():
    """Displays the main menu and handles user actions."""
    clear_terminal()
    members_list = []

    print("Welcom to Gym Management System\n")
    while True:
        print("\n1. Members dashboard")
        print("2. Search for a member")
        print("3. Display all members")
        print("4. Exit\n")
        main_choice = get_valid_choice("Enter your choice: ", range(1, 5))
        match main_choice:
            case 1:
                manage_members(members_list)
            case 2:
                search_results = search_member(members_list)
                if search_results == 4:
                    continue

                if search_results:
                    for member in search_results:
                        member.display_info()
                else:
                    print("No matching members found.")
            case 3:
                clear_terminal()
                if not members_list:
                    print("No members available to display.")
                else:
                    print("Displaying all members:\n" + "*" * 30)
                    for member in members_list:
                        member.display_info()
                        print("-" * 30)
                        time.sleep(0.5)
            case 4:
                clear_terminal()
                print("Exiting... Goodbye!")
                break


main_menu()
