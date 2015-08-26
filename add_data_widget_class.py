from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sqlite3

class AddDataWidget(QWidget):
    def __init__(self,db):
        super().__init__()
        self.layout = QVBoxLayout()

        self.database = db
        self.tables = QComboBox()
        self.table_view = QTableView()
        
        self.get_tables()
        
        for table in self.tables_list:
            self.tables.addItem(table[0])

    def get_tables(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            self.tables_list = cursor.fetchall()
        
