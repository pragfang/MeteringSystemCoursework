from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3

class EditType(QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database
        
        self.setWindowTitle("Edit Consumption Type")

        self.create_edit_type_layout()
        self.setCentralWidget(self.edit_type_widget)
        
    def create_edit_type_layout(self):
        self.select_type_label = QLabel("Select Consumption Type:")
        self.select_type_box = QComboBox()

        self.get_types()

        self.new_type_label = QLabel("New Consumption Type:")
        self.new_type_input = QLineEdit()

        self.new_description_label = QLabel("New Consumption Type Description:")
        self.new_description_input = QLineEdit()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_type_layout = QHBoxLayout()
        self.select_type_layout.addWidget(self.select_type_label)
        self.select_type_layout.addWidget(self.select_type_box)

        self.new_type_layout = QHBoxLayout()
        self.new_type_layout.addWidget(self.new_type_label)
        self.new_type_layout.addWidget(self.new_type_input)

        self.new_description_layout = QHBoxLayout()
        self.new_description_layout.addWidget(self.new_description_label)
        self.new_description_layout.addWidget(self.new_description_input)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.edit_type_layout = QVBoxLayout()
        self.edit_type_layout.addLayout(self.select_type_layout)
        self.edit_type_layout.addLayout(self.new_type_layout)
        self.edit_type_layout.addLayout(self.new_description_layout)
        self.edit_type_layout.addLayout(self.button_layout)

        self.edit_type_widget = QWidget()
        self.edit_type_widget.setLayout(self.edit_type_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.edit_data)

    def get_types(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ConsumptionType FROM Type")
            types = cursor.fetchall()
        self.select_type_box.clear()
        for Type in types:
            self.select_type_box.addItem(Type[0])

    def edit_data(self):
        Type = self.select_type_box.currentIndex() + 1
        new_type = self.new_type_input.text()
        new_description = self.new_description_input.text()
        
        if new_type != "":
            sql = "UPDATE Type SET ConsumptionTypeDescription=? WHERE TypeID=?"
            data = [new_description,Type]
            self.query(data,sql)
        if new_description != "":
            sql = "UPDATE Type SET ConsumptionTypeDescription=? WHERE TypeId=?"
            data = [new_description,Type]
            self.query(data,sql)
        self.close()

    def query(self,data,sql):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()
    
