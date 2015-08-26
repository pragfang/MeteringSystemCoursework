from PyQt4.QtSql import *
from PyQt4.QtGui import *

import sqlite3
import pdb

class DisplayTable(QWidget):
    def __init__(self,path):
        super().__init__()
        self.path = path
        self.db = None
        
        self.model = QSqlQueryModel()
        self.create_table_layout()

    def create_table_layout(self):
        self.table_view = QTableView()
        self.select_table_label = QLabel("Select Table:")
        self.select_table = QComboBox()
        self.select_type_label = QLabel("Select Type:")
        self.select_type = QComboBox()
        self.refresh_button = QPushButton("Refresh")

        self.select_type.setEnabled(False)

        self.select_table_layout = QHBoxLayout()
        self.select_table_layout.addWidget(self.select_table_label)
        self.select_table_layout.addWidget(self.select_table)

        self.select_type_layout = QHBoxLayout()
        self.select_type_layout.addWidget(self.select_type_label)
        self.select_type_layout.addWidget(self.select_type)

        self.table_layout = QVBoxLayout()
        self.table_layout.addLayout(self.select_table_layout)
        self.table_layout.addLayout(self.select_type_layout)
        self.table_layout.addWidget(self.refresh_button)
        self.table_layout.addWidget(self.table_view)

        self.setLayout(self.table_layout)
        
        self.select_table.currentIndexChanged.connect(self.update_table_view)
        self.select_type.currentIndexChanged.connect(self.update_table_view)
        self.refresh_button.clicked.connect(self.update_table_view)

    def open_database(self):
        if self.db:
            self.close_database()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        path = self.path
        self.db.setDatabaseName(path)
        ok = self.db.open()
        return ok

    def close_database(self):
        self.db.close()
        QSqlDatabase.removeDatabase("conn")

    def closeEvent(self, event):
        self.close_database()
    
    def get_types(self):
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ConsumptionType FROM Type")
            types = cursor.fetchall()
        self.select_type.clear()
        for Type in types:
            self.select_type.addItem(Type[0])
    
    def get_tables(self):
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            tables = cursor.fetchall()
        self.select_table.clear()
        for table in tables:
            self.select_table.addItem(table[0])

    def display_table(self,table,Type = None):
        model = QSqlTableModel()
        model.setTable(self.db.tables()[table])
##        if Type != None:
##            print("Type: {0}".format(Type))
##            if table == 5:
##                Filter = """SELECT * FROM Reading WHERE TypeID = {0}""".format(Type)
##            elif table == 1:
##                Filter = """SELECT * FROM Cost WHERE TypeCost.TypeID = {0}""".format(Type)
##            print(Filter)
##            model.setFilter(Filter)
        model.select()
        
        self.table_view.setModel(model)
        self.table_view.show()

    def update_table_view(self):
        table = self.select_table.currentIndex()
        print("table: {0}".format(table))
        if table == 1 or table == 5:
            #pdb.set_trace()
            self.select_type.setEnabled(True)
            Type = str(self.select_type.currentIndex() + 1)
            print(Type)
            self.display_table(table,Type)
        else:
            self.select_type.setEnabled(False)
            self.display_table(table)
        
