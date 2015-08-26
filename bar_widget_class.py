from PyQt4.QtGui import *

from reading_canvas_class import *
from graph_controller_class import *

import sqlite3
import pdb

class BarWidget(QWidget):
    def __init__(self,db):
        super().__init__()
        self.database = db
        self.graph_controller = GraphController(self.database)
        self.bar_canvas = ReadingCanvas()

        self.select_date_label = QLabel("Date:")
        self.select_date = QComboBox()
        
        self.select_table_label = QLabel("Table:")
        self.select_table = QComboBox()

        self.refresh_button = QPushButton("Refresh")

        self.combo_box_layout = QGridLayout()
        self.combo_box_layout.addWidget(self.select_table_label,1,1)
        self.combo_box_layout.addWidget(self.select_table,1,2)
        self.combo_box_layout.addWidget(self.select_date_label,2,1)
        self.combo_box_layout.addWidget(self.select_date,2,2)
        
        self.bar_layout = QVBoxLayout()
        self.bar_layout.addLayout(self.combo_box_layout)
        self.bar_layout.addWidget(self.refresh_button)
        self.bar_layout.addWidget(self.bar_canvas)

        self.setLayout(self.bar_layout)

        self.select_table.currentIndexChanged.connect(self.update_dates)
        self.select_table.activated.connect(self.update_dates)
        self.select_date.activated.connect(self.update_bar_chart)
        self.refresh_button.clicked.connect(self.update_bar_chart)

    def update_dates(self):
        self.get_dates()
        self.update_bar_chart()

    def update_bar_chart(self):
        #pdb.set_trace()
        date = self.select_date.currentText()
        table = self.select_table.currentText()
        self.graph_data(date,table)

    def get_tables(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            tables = cursor.fetchall()
        self.select_table.clear()
        self.cost_table = tables[1]
        self.reading_table = tables[5]
        tables = [self.cost_table,self.reading_table]
        for table in tables:
            self.select_table.addItem(table[0])

    def get_dates(self):
        table = self.select_table.currentText()
        if table == "Reading":
            date_entry = "ReadingDate"
            get_dates = True
        elif table == "Cost":
            date_entry = "CostStartDate"
            get_dates = True
        else:
            get_dates = False

        if get_dates:
            with sqlite3.connect(self.database) as db:
                cursor = db.cursor()
                cursor.execute("SELECT {0} FROM {1}".format(date_entry,table))
                dates = cursor.fetchall()
            self.select_date.clear()
            used_dates = []
            for date in dates:
                if date[0] not in used_dates:
                    self.select_date.addItem(date[0])
                    used_dates.append(date[0])

    def graph_data(self,date,table):
        totals = self.graph_controller.consumption_averages(date,table)
        self.bar_canvas.show_bar_graph(totals,date)
