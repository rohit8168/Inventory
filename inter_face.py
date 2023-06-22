import admin_level
import user_level

def admin_menu():
    print("Welcome!")
    print("1. View the data")
    print("2. View specific entry")
    print("3. Add data")
    print("4. Delete an entry")
    print("5. Update the data")
    print("6. Delete all")
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    return choice

def user_menu():
    print("-------------MENU-------------------")
    print("1. Buy a product and generate a bill")
    print("2. view products")
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    return choice

def admin_functionality(choice):
    if choice == 1:
        admin_level.displa()
    elif choice == 2:
        admin_level.specific()
    elif choice == 3:
        admin_level.add()
    elif choice == 4:
        admin_level.delete()
    elif choice == 5:
        admin_level.update()
    elif choice == 6:
        admin_level.del_all()
    else:
        print("Invalid choice!")

def user_functionality(choice):
    if choice == 1:
        user_level.gen_bill()
    elif choice == 2:
        admin_level.displa()
    else:
        print("Invalid choice!")

def fun():
    while True:
        n = input("Press 1 for admin and 0 for user: ")

        if n == '1':
            choice = admin_menu()
            if choice == 0:
                break
            admin_functionality(choice)
        elif n == '0':
            choice = user_menu()
            if choice == 0:
                break
            user_functionality(choice)
        else:
            print("Invalid choice!")

fun()
