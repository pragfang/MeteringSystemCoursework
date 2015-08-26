from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3
import pdb

class AddCost(QMainWindow):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setWindowTitle("Add Cost")

        self.create_add_cost_layout()
        self.setCentralWidget(self.add_cost_widget)

    def create_add_cost_layout(self):
        self.select_consumption_label = QLabel("Consumption Type:")
        self.select_consumption_box = QComboBox()

        self.get_types()
        
        self.cost_per_unit_label = QLabel("Cost Per Unit:")
        self.cost_per_unit_input = QLineEdit()

        self.cost_start_date_label = QLabel("Cost Start Date:")
        self.cost_start_date_input = QCalendarWidget()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_consumption_layout = QHBoxLayout()
        self.select_consumption_layout.addWidget(self.select_consumption_label)
        self.select_consumption_layout.addWidget(self.select_consumption_box)

        self.cost_per_unit_layout = QHBoxLayout()
        self.cost_per_unit_layout.addWidget(self.cost_per_unit_label)
        self.cost_per_unit_layout.addWidget(self.cost_per_unit_input)

        self.cost_start_date_layout = QHBoxLayout()
        self.cost_start_date_layout.addWidget(self.cost_start_date_label)
        self.cost_start_date_layout.addWidget(self.cost_start_date_input)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.add_cost_layout = QVBoxLayout()
        self.add_cost_layout.addLayout(self.select_consumption_layout)
        self.add_cost_layout.addLayout(self.cost_per_unit_layout)
        self.add_cost_layout.addLayout(self.cost_start_date_layout)
        self.add_cost_layout.addLayout(self.button_layout)

        self.add_cost_widget = QWidget()
        self.add_cost_widget.setLayout(self.add_cost_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.add_data)

    def get_types(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ConsumptionType FROM Type")
            self.consumption_types = cursor.fetchall()
        self.select_consumption_box.clear()
        for Type in self.consumption_types:
            self.select_consumption_box.addItem(Type[0])

    def get_id(self,Cost):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            sql = "SELECT CostID from Cost where CostPerUnit = {0}".format(Cost)
            cursor.execute(sql)
            CostID = cursor.fetchall()
            Cost = {Cost:CostID}
            return CostID
    
    def add_data(self):
        #pdb.set_trace()
        Type = str(self.select_consumption_box.currentIndex() + 1)
        Cost = self.cost_per_unit_input.text()
        Date = self.cost_start_date_input.selectedDate().toPyDate()

        sql = "INSERT INTO Cost(CostPerUnit, CostStartDate) VALUES (?,?)"
        data = [Cost,Date]
        self.query(data,sql)
        CostID = self.get_id(Cost)
        CostID = CostID[0]
        sql = "INSERT INTO TypeCost(CostID,TypeID) VALUES (?,?)"
        data = [str(CostID[0]),Type]
        self.query(data,sql)
        self.close()

    def query(self,data,sql):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()
