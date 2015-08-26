from PyQt4.QtGui import *

from reading_canvas_class import *
from graph_controller_class import *

import sqlite3

class ScatterWidget(QWidget):
    def __init__(self,db):
        super().__init__()
        self.database = db
        self.graph_controller = GraphController(self.database)
        self.scatter_canvas = ReadingCanvas()

        self.select_date_label = QLabel("Date")
        self.select_date = QComboBox()

        self.refresh_button = QPushButton("Refresh")

        self.combo_box_layout = QHBoxLayout()
        self.combo_box_layout.addWidget(self.select_date_label)
        self.combo_box_layout.addWidget(self.select_date)

        self.scatter_layout = QVBoxLayout()
        self.scatter_layout.addLayout(self.combo_box_layout)
        self.scatter_layout.addWidget(self.refresh_button)
        self.scatter_layout.addWidget(self.scatter_canvas)

        self.setLayout(self.scatter_layout)

        self.select_date.activated.connect(self.update_scatter_graph)
        self.refresh_button.clicked.connect(self.update_scatter_graph)

    def update_scatter_graph(self):
        date = self.select_date.currentText()
        self.get_dates()
        self.graph_data(date)

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

    def graph_data(self,date):
        totals = self.graph_controller.cost_of_readings(date)
        self.scatter_canvas.show_scatter_graph(totals,date)
