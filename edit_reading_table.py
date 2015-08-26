import sqlite3
from create_database import create_reading_table

def display_reading_menu():
    print()
    print("Edit Reading Table")
    print()
    print("1. Recreate the reading table")
    print("2. Add data to the reading table")
    print("3. Remove data from the reading table")
    print("4. Edit data in the reading table")
    print()

def get_reading_menu_choice(database):
    display_reading_menu()
    choice = input("Please select an option from the menu [1-4]: ")
    if choice == "1":
        create_reading_table(database)

    elif choice == "2":
        Reading = input("What is the reading you would like to add? ")
        Date = input("What is the date of the reading? ")
        DataList = [(Reading, Date)]
        add_data(DataList,database)

    elif choice == "3":
        Readings = get_data(database)
        print("Availabe readings:")
        for Reading in Readings:
            print(Reading)
        print()
        ID = input("What is the ID of the data you would like to remove from the reading table? ")
        remove_data((ID,),database)

    elif choice == "4":
        Readings = get_data(database)
        print("Availabe readings:")
        for Reading in Readings:
            print(Reading)
        ID = input("What is the ID of the reading you would like to change? ")
        Data = input("What is the new reading you would like to add? ")
        Date = input("What is the new date of the reading? ")
        DataList = [(Data,Date,ID)]
        update_data(DataList,database)

def get_data(database):
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        cursor.execute("select * from Reading")
        Readings = cursor.fetchall()
        return Readings

def add_data(DataList,database):
    sql = "insert into Reading(ConsumptionReading,ReadingDate) values (?,?)"
    for record in DataList:
        query(sql,database,record)

def remove_data(data,database):
    sql = "delete from Reading where ReadingID=?"
    query(sql,database,data)

def update_data(data,database):
    sql = "update Reading set ConsumptionReading=?, ReadingDate=? where ReadingID=?"
    for record in data:
        query(sql,database,record)

def query(sql,database,data):
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()
