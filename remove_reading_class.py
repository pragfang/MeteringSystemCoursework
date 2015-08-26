from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3

class RemoveReading(QMainWindow):
    def __init__(self,db):
        super().__init__()

        self.database = db
        
        self.setWindowTitle("Remove Reading")

        self.create_remove_reading_layout()
        self.setCentralWidget(self.remove_reading_widget)

    def create_remove_reading_layout(self):
        self.select_reading_label = QLabel("Select Reading:")
        self.select_reading = QComboBox()

        self.get_readings()
        
        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_reading_layout = QHBoxLayout()
        self.select_reading_layout.addWidget(self.select_reading_label)
        self.select_reading_layout.addWidget(self.select_reading)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.remove_reading_layout = QVBoxLayout()
        self.remove_reading_layout.addLayout(self.select_reading_layout)
        self.remove_reading_layout.addLayout(self.button_layout)

        self.remove_reading_widget = QWidget()
        self.remove_reading_widget.setLayout(self.remove_reading_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.remove_reading)

    def get_readings(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ReadingID,ConsumptionReading FROM Reading")
            readings = cursor.fetchall()
        self.select_reading.clear()
        for reading in readings:
            self.select_reading.addItem("{0}: {1}".format(reading[0],reading[1]))

    def remove_reading(self):
        Reading = self.select_reading.currentText()
        Reading = Reading.partition(":")
        Reading = Reading[0]
        sql = "DELETE from Reading WHERE ReadingID = ?"
        self.query(sql,Reading)
        self.close()

    def query(self,sql,Reading):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,Reading)
            db.commit()
        
