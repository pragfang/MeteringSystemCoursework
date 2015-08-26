from PyQt4.QtGui import *

from reading_canvas_class import *
from graph_controller_class import *

import sqlite3
import pdb

class LineWidget(QWidget):
    def __init__(self,db):
        super().__init__()
        self.database = db
        self.graph_controller = GraphController(self.database)
        self.line_canvas = ReadingCanvas()

        self.select_table_label = QLabel("Table")
        self.select_table = QComboBox()
        self.select_type_label = QLabel("Type")
        self.select_type = QComboBox()
        self.select_date_label = QLabel("Date")
        self.select_date = QComboBox()

        self.refresh_button = QPushButton("Refresh")

        self.combo_box_layout = QGridLayout()
        self.combo_box_layout.addWidget(self.select_table_label,1,1)
        self.combo_box_layout.addWidget(self.select_table,1,2)
        self.combo_box_layout.addWidget(self.select_date_label,2,1)
        self.combo_box_layout.addWidget(self.select_date,2,2)

        self.line_layout = QVBoxLayout()
        self.line_layout.addLayout(self.combo_box_layout)
        self.line_layout.addWidget(self.refresh_button)
        self.line_layout.addWidget(self.line_canvas)

        self.setLayout(self.line_layout)

        self.select_table.currentIndexChanged.connect(self.update_dates)
        self.select_table.activated.connect(self.update_dates)
        self.select_type.activated.connect(self.update_line_graph)
        self.select_date.activated.connect(self.update_line_graph)
        self.refresh_button.clicked.connect(self.update_line_graph)

    def update_dates(self):
        self.get_dates()
        self.get_types()
        self.update_line_graph()

    def update_line_graph(self):
        table = self.select_table.currentText()
        Type = self.select_type.currentText()
        date = self.select_date.currentText()
        print(table)
        print(Type)
        print(date)
        #pdb.set_trace()
        self.graph_data(date,table,Type)

    def get_tables(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            tables = cursor.fetchall()
        self.select_table.clear()
        self.cost_table = tables[1]
        self.reading_table = tables[5]
        tables = [self.reading_table,self.cost_table]
        for Table in tables:
            self.select_table.addItem(Table[0])

    def get_types(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT ConsumptionType FROM Type")
            Types = cursor.fetchall()
        self.select_type.clear()
        for Type in Types:
            self.select_type.addItem(Type[0])

    def get_dates(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("""SELECT Cost.CostStartDate FROM Cost,Reading
                           WHERE Cost.CostStartDate = Reading.ReadingDate""")
            dates = cursor.fetchall()

        self.select_date.clear()
        used_dates = []
        for date in dates:
            if date[0] not in used_dates:
                self.select_date.addItem(date[0])
                used_dates.append(date[0])

    def graph_data(self,date,table,Type):
        #pdb.set_trace()
        totals = self.graph_controller.readings_over_time(date,table,Type)
        self.line_canvas.show_line_graph(totals,date)
