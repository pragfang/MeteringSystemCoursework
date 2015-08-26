from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import sqlite3

class AddData(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.database = db
        self.table = None
        self.type = None
        self.status_bar = QStatusBar()
        
        self.setWindowTitle("Add Data")

        self.stacked_layout = QStackedLayout()
        
        self.create_add_data_layout()
        self.stacked_layout.addWidget(self.add_data_widget)
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        self.stacked_layout.setCurrentIndex(0)
        
    def create_add_data_layout(self):
        if not hasattr(self, "add_data_layout"):
            self.table_label = QLabel("Data Table:")
            self.type_label = QLabel("Consumption Type:")
            self.data_type_label = QLabel("Data Type:")
            self.data_label_a = QLabel("Data A:")
            self.data_label_b = QLabel("Data B:")
            self.data_label_c = QLabel("Data C:")
            self.select_table = QComboBox()
            self.select_consumption_type = QComboBox()
            self.select_data_type = QComboBox()
            self.data_input_a = QLineEdit()
            self.data_input_b = QLineEdit()
            self.data_input_c = QLineEdit()
            self.proceed_button = QPushButton("Proceed")
            self.back_button = QPushButton("Back")

            self.select_consumption_type.setEnabled(False)
            self.select_data_type.setEnabled(False)
            self.data_input_a.setEnabled(False)
            self.data_input_b.setEnabled(False)
            self.data_input_c.setEnabled(False)
            
            self.get_tables()
            self.get_consumption_types()
            self.update_table_data()
            
            self.consumption_a = self.consumption_types[0]
            self.consumption_b = self.consumption_types[1]
            self.consumption_c = self.consumption_types[2]
            
            self.select_consumption_type.addItem("None")
            self.select_consumption_type.addItem(self.consumption_a[0])
            self.select_consumption_type.addItem(self.consumption_b[0])
            self.select_consumption_type.addItem(self.consumption_c[0])

            self.user_table = self.tables[0]
            self.cost_table = self.tables[1]
            self.type_table = self.tables[4]
            self.reading_table = self.tables[5]
            
            self.select_table.addItem("None")
            self.select_table.addItem(self.user_table[0])
            self.select_table.addItem(self.cost_table[0])
            self.select_table.addItem(self.type_table[0])
            self.select_table.addItem(self.reading_table[0])

            self.select_data_type.addItem("None")

            self.selection_layout = QGridLayout()
            self.selection_layout.addWidget(self.table_label,1,1)
            self.selection_layout.addWidget(self.type_label,2,1)
            self.selection_layout.addWidget(self.select_table,1,2)
            self.selection_layout.addWidget(self.select_consumption_type,2,2)

            self.input_layout = QHBoxLayout()
            self.input_layout.addWidget(self.data_type_label)
            self.input_layout.addWidget(self.select_data_type)

            self.data_layout_a = QHBoxLayout()
            self.data_layout_a.addWidget(self.data_label_a)
            self.data_layout_a.addWidget(self.data_input_a)

            self.data_layout_b = QHBoxLayout()
            self.data_layout_b.addWidget(self.data_label_b)
            self.data_layout_b.addWidget(self.data_input_b)

            self.data_layout_c = QHBoxLayout()
            

            self.button_layout = QHBoxLayout()
            self.button_layout.addWidget(self.proceed_button)
            self.button_layout.addWidget(self.back_button)

            self.add_data_layout = QVBoxLayout()
            self.add_data_layout.addLayout(self.selection_layout)
            self.add_data_layout.addLayout(self.input_layout)
            self.add_data_layout.addLayout(self.data_layout_a)
            self.add_data_layout.addLayout(self.button_layout)
            
            self.add_data_widget = QWidget()
            self.add_data_widget.setLayout(self.add_data_layout)

            self.proceed_button.clicked.connect(self.check_data)
            self.back_button.clicked.connect(self.close)
            self.select_table.activated.connect(self.update_table_data)
            self.select_data_type.activated.connect(self.update_data_input)
        else:
            self.stacked_layout.setCurrentIndex(0)

    def update_table_data(self):
        table = self.select_table.currentText()
        
        if table != "" and table !="None":
            if table == "User" or table == "Type":
                self.select_consumption_type.setEnabled(False)
            else:
                self.select_consumption_type.setEnabled(True)
            self.select_data_type.setEnabled(True)
            self.data_input_a.setEnabled(True)
            self.get_table_data(table)

            self.select_data_type.clear()
            self.select_data_type.addItem("None")
            for item in self.data_types:
                if "ID" not in item[1]:
                    self.select_data_type.addItem(item[1])
        else:
            self.select_consumption_type.setEnabled(False)
            self.select_data_type.setEnabled(False)
            self.data_input_a.setEnabled(False)

    def update_data_input(self):
        data_type = self.select_data_type.currentText()

        self.data_input_a.clear()

        if data_type !="" and data_type !="None":
            self.data_input_a.setEnabled(True)
            if "Name" in data_type:
                self.data_input_a.setMaxLength(20)
            elif "Password" in data_type:
                self.data_input_a.setMaxLength(16)
            else:
                self.data_input_a.setMaxLength(10)
        else:
            self.data_input.setEnabled(False)

    def get_tables(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            self.tables = cursor.fetchall()

    def get_table_data(self,table):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA table_info({0})".format(table))
            self.data_types = cursor.fetchall()
    
    def get_consumption_types(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ConsumptionType FROM Type")
            self.consumption_types = cursor.fetchall()

    def check_data(self):
        if self.data_input_a.isEnabled():
            text_a = self.data_input_a.text()
            if text_a != "":
                data_type = self.select_data_type.currentText()
                table = self.select_table.currentText()
                self.add_data(text_a,data_type,table)

    def add_data(self,text,data_type,table):
        sql = "insert into {0}({1}) values (?)".format(table,data_type)
        print(sql)
        self.query(sql,str(text))
        
    def query(self,sql,data):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,(data,))
            db.commit()

    def set_user_table(self):
        self.select_table.setText(self.user_table[0])
        self.table = self.user_table[0]
        self.set_consumption_none()
        self.get_table_data()

    def set_cost_table(self):
        self.select_table.setText(self.cost_table[0])
        self.table = self.cost_table[0]
        self.get_table_data()

    def set_type_table(self):
        self.select_table.setText(self.type_table[0])
        self.table = self.type_table[0]
        self.set_consumption_none()
        self.get_table_data()

    def set_reading_table(self):
        self.select_table.setText(self.reading_table[0])
        self.table = self.reading_table[0]
        self.get_table_data()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddData("ConsumptionMeteringSystem.db")
    window.show()
    window.raise_()
    application.exec_()
    
