from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sqlite3

class DisplayTable(QWidget):
    def __init__(self, db):
        super().__init__()
        self.database = db
        self.layout = QVBoxLayout()
        self.model = None
        self.query = None
        self.display_table_layout()
        self.setLayout(self.layout)
        
    def display_table_layout(self):
        if not hasattr(self,"select_table"):
            self.table_view = QTableView()
            self.select_table_label = QLabel("Select Table:")
            self.select_table = QComboBox()

            self.select_table_layout = QHBoxLayout()
            self.select_table_layout.addWidget(self.select_table_label)
            self.select_table_layout.addWidget(self.select_table)

            self.layout.addLayout(self.select_table_layout)
            self.layout.addWidget(self.table_view)
        if self.database != "None":
            self.get_table_data()

    def show_results(self):
        if not self.model or not isinstance(self.model,QSqlQueryModel):
            self.model = QSqlQueryModel()
        self.model.setQuery(self.query)
        self.table_view.setModel(self.model)
        self.table_view.show()

    def get_tables(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            tables = cursor.fetchall()
        self.select_table.clear()
        tables.pop(3)
        tables.pop(2)
        for table in tables:
            self.select_table.addItem(table[0])

    def get_table_data(self):
        table = self.select_table.currentText()
        self.query = "SELECT * FROM {0}".format(table)
        self.show_results()

    def update_results(self,db):
        self.database = db
        self.get_tables()
        self.display_table_layout()
