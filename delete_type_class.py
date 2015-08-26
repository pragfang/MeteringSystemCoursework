from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3

class DeleteType(QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database
        
        self.setWindowTitle("Delete Consumption Type")

        self.create_delete_type_layout()
        self.setCentralWidget(self.delete_type_widget)

    def create_delete_type_layout(self):
        self.select_type_label = QLabel("Select Consumption Type:")
        self.select_type_box = QComboBox()

        self.get_types()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_type_layout = QHBoxLayout()
        self.select_type_layout.addWidget(self.select_type_label)
        self.select_type_layout.addWidget(self.select_type_box)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.delete_type_layout = QVBoxLayout()
        self.delete_type_layout.addLayout(self.select_type_layout)
        self.delete_type_layout.addLayout(self.button_layout)

        self.delete_type_widget = QWidget()
        self.delete_type_widget.setLayout(self.delete_type_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.delete_data)

    def get_types(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ConsumptionType FROM Type")
            types = cursor.fetchall()
        self.select_type_box.clear()
        for Type in types:
            self.select_type_box.addItem(Type[0])

    def delete_data(self):
        Type = str(self.select_type_box.currentIndex() + 1)
        sql = "DELETE from Type WHERE TypeID = ?"
        self.query(sql,Type)
        self.close()

    def query(self,sql,Type):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA Foreign_Keys = ON")
            cursor.execute(sql,Type)
            db.commit()
