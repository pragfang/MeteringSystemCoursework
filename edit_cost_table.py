import sqlite3
from create_database import create_cost_table

def display_cost_menu():
    print()
    print("Edit Cost Table")
    print()
    print("1. Recreate the cost table")
    print("2. Add data to the cost table")
    print("3. Remove data from the cost table")
    print("4. Edit data in the cost table")
    print()

def get_cost_menu_choice(database):
    display_cost_menu()
    choice = input("Please select an option from the menu [1-4]: ")
    if choice == "1":
        create_reading_table(database)

    elif choice == "2":
        Cost = input("What is the price per unit? ")
        CostDate = input("What is the starting date of this price? ")
        DataList = [(Cost, CostDate)]
        add_data(DataList,database)

    elif choice == "3":
        Costs = get_data(database)
        print("Available costs:")
        for Cost in Costs:
            print(Cost)
        print()
        ID = input("What is the ID of the cost you would like to remove from the cost table? ")
        remove_data((ID,),database)

    elif choice == "4":
        Costs = get_data(database)
        print("Available costs:")
        for Cost in Costs:
            print(Cost)
        print()
        ID = input("What is the ID of the cost you would like to change? ")
        Cost = input("What is the new price per unit? ")
        CostDate = input("What is the new starting date of this price? ")
        DataList = [(Cost,CostDate,ID)]
        update_data(DataList,database)

def get_data(database):
    with sqlite3.connect(database) as db:
        cursor = db.cursor
        cursor.execute("Select * from Cost")
        Costs = cursor.fetchall()
        return Costs

def add_data(DataList,database):
    sql = "insert into Cost(CostPerUnit,CostStartDate) values (?,?)"
    for record in DataList:
        query(sql,database,record)

def remove_data(data,database):
    sql = "delete from Cost where CostID=?"
    query(sql,database,data)

def update_data(data,database):
    sql = "update User set CostPerUnit=?,CostStartDate=? where CostID=?"
    for record in data:
        query(sql,database,record)

def query(sql,database,data):
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()
