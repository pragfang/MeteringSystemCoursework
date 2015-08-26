from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3

class AddReading(QMainWindow):
    def __init__(self,db):
        super().__init__()

        self.database = db

        self.setWindowTitle("Add Reading")

        self.create_add_reading_layout()
        self.setCentralWidget(self.add_reading_widget)

    def create_add_reading_layout(self):
        self.type_label = QLabel("Consumption Type:")
        self.select_type = QComboBox()

        self.get_types()
        
        self.reading_label = QLabel("Consumption Reading:")
        self.reading_input = QLineEdit()

        self.date_label = QLabel("Reading Date:")
        self.date_input = QCalendarWidget()
        
        self.confirm_button = QPushButton("Confirm")
        self.back_button = QPushButton("Back")

        self.select_type_layout = QHBoxLayout()
        self.select_type_layout.addWidget(self.type_label)
        self.select_type_layout.addWidget(self.select_type)

        self.input_reading_layout = QHBoxLayout()
        self.input_reading_layout.addWidget(self.reading_label)
        self.input_reading_layout.addWidget(self.reading_input)

        self.input_date_layout = QHBoxLayout()
        self.input_date_layout.addWidget(self.date_label)
        self.input_date_layout.addWidget(self.date_input)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.add_reading_layout = QVBoxLayout()
        self.add_reading_layout.addLayout(self.select_type_layout)
        self.add_reading_layout.addLayout(self.input_reading_layout)
        self.add_reading_layout.addLayout(self.input_date_layout)
        self.add_reading_layout.addLayout(self.button_layout)

        self.add_reading_widget = QWidget()
        self.add_reading_widget.setLayout(self.add_reading_layout)

        self.confirm_button.clicked.connect(self.add_data)
        self.back_button.clicked.connect(self.close)

    def get_types(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT TypeID,ConsumptionType FROM Type")
            self.consumption_types = cursor.fetchall()
        self.select_type.clear()
        for Type in self.consumption_types:
            self.select_type.addItem("{0}. {1}".format(Type[0],Type[1]))
        
    def add_data(self):
        Type = self.select_type.currentText()
        Type = Type[0]
        Reading = self.reading_input.text()
        Date = self.date_input.selectedDate().toPyDate()
        sql = "INSERT INTO Reading(ConsumptionReading, ReadingDate, TypeID) VALUES (?,?,?)"
        data = [Reading,Date,Type]
        self.query(data,sql)
        self.close()

    def query(self,data,sql):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()
        
