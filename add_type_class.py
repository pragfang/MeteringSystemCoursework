from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3

class AddType(QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database
        
        self.setWindowTitle("Add Consumption Type")

        self.create_type_layout()
        self.setCentralWidget(self.type_widget)

    def create_type_layout(self):
        self.type_label = QLabel("Consumption Type:")
        self.type_input = QLineEdit()

        self.description_label = QLabel("Consumption Type Description")
        self.description_input = QLineEdit()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.add_type_layout = QGridLayout()
        self.add_type_layout.addWidget(self.type_label,1,1)
        self.add_type_layout.addWidget(self.type_input,1,2)
        self.add_type_layout.addWidget(self.description_label,2,1)
        self.add_type_layout.addWidget(self.description_input,2,2)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.type_layout = QVBoxLayout()
        self.type_layout.addLayout(self.add_type_layout)
        self.type_layout.addLayout(self.button_layout)

        self.type_widget = QWidget()
        self.type_widget.setLayout(self.type_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.add_data)

    def add_data(self):
        Type = self.type_input.text()
        Description = self.description_input.text()

        sql = "INSERT INTO Type(ConsumptionType, ConsumptionTypeDescription) VALUES (?,?)"
        data = [Type,Description]
        self.query(data,sql)
        self.close()

    def query(self,data,sql):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()
