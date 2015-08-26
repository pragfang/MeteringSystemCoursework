import sqlite3

def create_table(database,sql,table_name):
    with sqlite3.connect(database) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? (y/n) ".format(table_name))
            response = response.lower()
            if response == "y":
                keep_table = False
                print("The table {0} will be recreated - all existing data will be lost.".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The table {0} will be kept.".format(table_name))
        else:
            keep_table = False
    if not keep_table:
        cursor.execute(sql)
        db.commit()
        print("The table {0} has been created successfully!".format(table_name))

def create_type_table(database):
    sql = """create table Type
             (TypeID integer,
             ConsumptionType text,
             ConsumptionTypeDescription text,
             primary key(TypeID))"""
    create_table(database,sql,"Type")

def create_reading_table(database):
    sql = """create table Reading
             (ReadingID integer,
             ConsumptionReading real,
             ReadingDate text,
             TypeID integer,
             primary key(ReadingID)
             foreign key(TypeID) references Type(TypeID))"""
    create_table(database,sql,"Reading")

def create_userreading_table(database):
    sql = """create table UserReading
             (UserReadingID integer,
             UserID integer,
             ReadingID integer,
             primary key(UserReadingID)
             foreign key(UserID) references User(UserID)
             foreign key(ReadingID) references Reading(ReadingID))"""
    create_table(database,sql,"UserReading")

def create_user_table(database):
    sql = """create table User
             (UserID integer,
             FirstName text,
             LastName text,
             UserPassword text,
             primary key(UserID))"""
    create_table(database,sql,"User")

def create_cost_table(database):
    sql = """create table Cost
             (CostID integer,
             CostPerUnit real,
             CostStartDate text,
             primary key(CostID))"""
    create_table(database,sql,"Cost")

def create_typecost_table(database):
    sql = """create table TypeCost
             (TypeCostID integer,
             TypeID integer,
             CostID integer,
             primary key(TypeCostID)
             foreign key(CostID) references Cost(CostID)
             foreign key(TypeID) references Type(TypeID))"""
    create_table(database,sql,"TypeCost")

if __name__ == "__main__":
    database = "ConsumptionMeteringSystem.db"
    create_type_table(database)
    create_reading_table(database)
    create_user_table(database)
    create_cost_table(database)
    create_userreading_table(database)
    create_typecost_table(database)
