# ----------------------------------- #
# -- Membership Control Application --#
# ----------------------------------- #

admins = []
users = []

print('='*40)
print("Membership Control Application".center(40))
print('='*40)

# Program Progress

admin1 = input("Add the first admin: ").strip().lower()
admins.append(admin1)
print(f"Welcome Mr {admins[0]}")

mainMenu = int(input("1- Add new admin\n2- Add new user\n3- Delete admin\n4- Delete user\n\
5- Exit\n6- Logout\nEnter number from 1 to 6: "))

if mainMenu == 1:
    admin1= input("Enter the name of the admin: ")
    admins.append(admin1)
    print("The new admin was added successfully!")
    print(f"Admin list is: {admins}")
    print(mainMenu)
elif mainMenu == 2:
    user1= input("Enter the name of the user: ")
    users.append(user1)
    print("The new user was added successfully!")
    print(f"User list is: {users}")
    print("We were glad to help you sir!")
elif mainMenu == 3:
    admin1= input("Enter the name of the admin: ")
    if admin1 in admins:
        admins.remove(admin1)
        print("The admin was removed successfully!")
        print("We were glad to help you sir!")
    else:
        print("Admin not exists!")
        admin1= input("Enter the name of the admin: ")
        if admin1 in admins:
            admins.remove(admin1)
            print("The admin was removed successfully!")
            print("We were glad to help you sir!")
        else:
            print("Admin not exists!\nWe have to end the program")
elif mainMenu == 4:
    user1= input("Enter the name of the user: ")
    if user1 in users:
        users.remove(user1)
        print("The user was removed successfully!")
        print("We were glad to help you sir!")
        
    else:
        print("Admin not exists!")
        user1= input("Enter the name of the user: ")
        if user1 in users:
            users.remove(user1)
            print("The user was removed successfully!")
            print("We were glad to help you sir!")
        else:
            print("Admin not exists!\nWe have to end the program")
elif mainMenu == 5:
    print("We are were to help you sir!")
    exit
elif mainMenu == 6:
    print('='*40)
    print("Membership Control Application".center(40))
    print('='*40)
    admin1 = input("Enter your name: ").strip().lower()
    if admin1 in admins:
        print(f"Welcome Back Mr {admin1}")
        mainMenu = int(input("1- Show admin list\n2- Show user list\n\
3- Add new admin\n4- Add new user\n5- Delete admin\n6- Delete user\n\
7- Exit\nEnter number from 1 to 7: "))
        
        if mainMenu == 1:
            print(admins)
            print("We were glad to help you sir!")
        elif mainMenu == 2:
            print(users)
            print("We were glad to help you sir!")
        elif mainMenu == 3:
            admin1= input("Enter the name of the admin: ")
            admins.append(admin1)
            print("The new admin was added successfully!")
            print(f"Admin list is: {admins}")
            print("We were glad to help you sir!")
        elif mainMenu == 4:
            user1= input("Enter the name of the user: ")
            users.append(user1)
            print("The new user was added successfully!")
            print(f"User list is: {users}")
            print("We were glad to help you sir!")
        elif mainMenu == 5:
            admin1= input("Enter the name of the admin: ")
            if admin1 in admins:
                admins.remove(admin1)
                print("The admin was removed successfully!")
                print("We were glad to help you sir!")
            else:
                print("Admin not exists!")
                admin1= input("Enter the name of the admin: ")
                if admin1 in admins:
                    admins.remove(admin1)
                    print("The admin was removed successfully!")
                    print("We were glad to help you sir!")
                else:
                    print("Admin not exists!\nWe have to end the program")
        elif mainMenu == 6:
            user1= input("Enter the name of the user: ")
            if user1 in users:
                users.remove(user1)
                print("The user was removed successfully!")
                print("We were glad to help you sir!")
                
            else:
                print("Admin not exists!")
                user1= input("Enter the name of the user: ")
                if user1 in users:
                    users.remove(user1)
                    print("The user was removed successfully!")
                    print("We were glad to help you sir!")
                else:
                    print("Admin not exists!\nWe have to end the program")
        elif mainMenu == 7:
            print("We are were glad to help you sir!")
            exit
    elif admin1 in users:
        print(f"Welcome Mr {admin1}\nUnfortunatly We don't have any services yet!")
        print("Come back soon!")
        exit         
    else:
        print("Sorry the user not exists!")
        exit
else:
    print("Invalid input!")
    exit  