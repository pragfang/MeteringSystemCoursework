from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3

class EditCost(QMainWindow):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setWindowTitle("Edit Cost")

        self.create_edit_cost_layout()
        self.setCentralWidget(self.edit_cost_widget)

    def create_edit_cost_layout(self):
        self.select_cost_label = QLabel("Select Cost:")
        self.select_cost_box = QComboBox()

        self.get_data()

        self.new_cost_label = QLabel("New Cost Per Unit:")
        self.new_cost_input = QLineEdit()

        self.new_cost_date_label = QLabel("New Cost Start Date:")
        self.new_cost_date_selection = QCalendarWidget()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_cost_layout = QHBoxLayout()
        self.select_cost_layout.addWidget(self.select_cost_label)
        self.select_cost_layout.addWidget(self.select_cost_box)

        self.new_cost_layout = QHBoxLayout()
        self.new_cost_layout.addWidget(self.new_cost_label)
        self.new_cost_layout.addWidget(self.new_cost_input)

        self.new_date_layout = QHBoxLayout()
        self.new_date_layout.addWidget(self.new_cost_date_label)
        self.new_date_layout.addWidget(self.new_cost_date_selection)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.edit_cost_layout = QVBoxLayout()
        self.edit_cost_layout.addLayout(self.select_cost_layout)
        self.edit_cost_layout.addLayout(self.new_cost_layout)
        self.edit_cost_layout.addLayout(self.new_date_layout)
        self.edit_cost_layout.addLayout(self.button_layout)

        self.edit_cost_widget = QWidget()
        self.edit_cost_widget.setLayout(self.edit_cost_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.edit_data)

    def get_data(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT CostID,CostPerUnit FROM Cost")
            costs = cursor.fetchall()
        self.select_cost_box.clear()
        for cost in costs:
            self.select_cost_box.addItem("{0}: {1}".format(cost[0],cost[1]))
        
    def edit_data(self):
        Cost = self.select_cost_box.currentText()
        Cost = Cost.partition(":")
        Cost = Cost[0]
        new_cost = self.new_cost_input.text()
        new_date = self.new_cost_date_selection.selectedDate().toPyDate()

        if new_cost != "":
            sql = "UPDATE Cost SET CostPerUnit=? WHERE CostID=?"
            data = [new_cost,str(Cost)]
            self.query(data,sql)
        if new_date != "":
            sql = "UPDATE Cost SET CostStartDate=? WHERE CostID=?"
            data = [new_date,Cost]
            self.query(data,sql)
        self.close()

    def query(self,data,sql):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()
