from PyQt4.QtGui import *
from PyQt4.QtCore import *

from add_data_class import *
from remove_data_class import *
from format_database_class import *

class HomeToolBar(QToolBar):
    def __init__(self,database_open,db):
        super().__init__()

        self.database_open = database_open
        self.database = db
        
        self.open_database = self.addAction("Open Database")
        self.close_database = self.addAction("Close Database")
        self.create_database = self.addAction("Create Database")
        self.format_database = self.addAction("Format Database")
        self.add_data = self.addAction("Add Data")
        self.remove_data = self.addAction("Remove Data")

        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)
        self.create_database.triggered.connect(self.new_database)
        self.format_database.triggered.connect(self.clear_database)
        self.add_data.triggered.connect(self.insert_data)
        self.remove_data.triggered.connect(self.delete_data)

    def open_connection(self):
        pass

    def close_connection(self):
        pass

    def new_database(self):
        pass

    def clear_database(self):
        if self.database_open == True:
            if not hasattr(self,"FormatDatabase"):
                self.FormatDatabase = FormatDatabase()
            self.FormatDatabase.show()
            self.FormatDatabase.raise_()
        else:
            print("database is not open")

    def insert_data(self):
        if self.database_open == True:
            if not hasattr(self,"AddData"):
                self.AddData = AddData(self.database)
            self.AddData.show()
            self.AddData.raise_()
        else:
            print("database is not open")

    def delete_data(self):
        if self.database_open == True:
            if not hasattr(self,"RemoveData"):
                self.RemoveData = RemoveData()
                self.RemoveData.show()
                self.RemoveData.raise_()
        else:
            print("database is not open")

if __name__ == "__main__":
    print("Hello")
    test = HomeToolBar()
    print(test)
