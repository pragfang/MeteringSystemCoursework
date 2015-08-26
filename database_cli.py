from create_database import *
from edit_type_table import *
from edit_reading_table import *
from edit_user_table import *
from edit_cost_table import *

def display_menu():
    print()
    print("Main Menu")
    print()
    print("1. (Re)Create database")
    print("2. Edit Type Table")
    print("3. Edit Reading Table")
    print("4. Edit User Table")
    print("5. Edit Cost Table")
    print("0. Quit.")
    print()

def get_menu_choice():
    display_menu()
    choice = input("Please select an option from the menu [1-5 or 0 to Quit]: ")
    if choice == "1":
        create_type_table(database)
        create_reading_table(database)
        create_user_table(database)
        create_cost_table(database)
        create_userreading_table(database)
        create_typecost_table(database)

    elif choice == "2":
        get_type_menu_choice(database)

    elif choice == "3":
        get_reading_menu_choice(database)

    elif choice == "4":
        get_user_menu_choice(database)

    elif choice == "5":
        get_cost_menu_choice(database)

    elif choice == "0":
        Quit = True
        return Quit

if __name__ == "__main__":
    database = "ConsumptionMeteringSystem.db"
    Quit = False
    while not Quit:
        Quit = get_menu_choice()
        
