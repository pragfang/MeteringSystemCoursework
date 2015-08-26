import sqlite3
import numpy as np
import sys

from PyQt4.QtGui import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class Controller:
    def __init__(self,path):
        self.path = path

    def query(self,sql,parameters=None):
        with sqlite3.connect(self.path) as self.db:
            cursor = self.db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            if parameters != None:
                cursor.execute(sql,parameters)
            else:
                cursor.execute(sql)
            results = cursor.fetchall()
            return results

    def consumption_totals(self,date):
        sql = """SELECT Type.ConsumptionType, sum(Reading.ConsumptionReading) as total
                 FROM Type, Reading
                 WHERE Type.TypeID = Reading.TypeID and
                 Reading.ReadingDate = ?
                 GROUP BY Type.ConsumptionType"""
        return self.query(sql,[date])

class ReadingCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(1,1,1)
        super().__init__(self.fig)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.fig.canvas.draw()

    def show_bar_graph(self,data,date):
        self.ax.clear()
        data_dict = dict(data)
        for i, key in enumerate(data_dict):
            self.ax.bar(i,data_dict[key])
        self.ax.set_xticks(np.arange(len(data_dict))+0.4)
        self.ax.set_xticklabels(list(data_dict.keys()))
        self.fig.autofmt_xdate()
        self.ax.set_title("Total Consumption for {0}".format(date))
        self.ax.set_xlabel("Type")
        self.ax.set_ylabel("Consumption")
        self.fig.canvas.draw()

    def show_pie_chart(self,data,date):
        self.ax.clear()
        data_dict = dict(data)
        data = list(data_dict.values())
        labels = list(data_dict.keys())
        self.ax.pie(data,labels=labels,autopct='%1.1f%%')
        self.ax.set_title("Percentage Consumption for {0}".format(date))
        self.fig.canvas.draw()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graphing Prototypes")

        self.stacked_layout = QStackedLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)

        self.menu_bar = QMenuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.graph_menu = self.menu_bar.addMenu("Select Graph Type")
        
        self.open_database = self.file_menu.addAction("Open Database")
        self.select_bar = self.graph_menu.addAction("Display Bar Chart")
        self.select_pie = self.graph_menu.addAction("Display Pie Chart")

        self.bar_canvas = ReadingCanvas()
        self.pie_canvas = ReadingCanvas()

        self.bar_layout = QVBoxLayout()
        self.bar_layout.addWidget(self.bar_canvas)
        self.bar_widget = QWidget()
        self.bar_widget.setLayout(self.bar_layout)
        self.stacked_layout.addWidget(self.bar_widget)

        self.pie_layout = QVBoxLayout()
        self.pie_layout.addWidget(self.pie_canvas)
        self.pie_widget = QWidget()
        self.pie_widget.setLayout(self.pie_layout)
        self.stacked_layout.addWidget(self.pie_widget)

        self.setMenuWidget(self.menu_bar)
        self.setCentralWidget(self.central_widget)

        self.stacked_layout.setCurrentIndex(0)

        self.open_database.triggered.connect(self.load_database)
        self.select_bar.triggered.connect(self.set_bar_chart)
        self.select_pie.triggered.connect(self.set_pie_chart)

    def load_database(self):
        path = QFileDialog.getOpenFileName(caption="Open Database")
        self.controller = Controller(path)
        self.graph_data()

    def graph_data(self):
        totals = self.controller.consumption_totals("2015-01-26")
        self.pie_canvas.show_pie_chart(totals,"2015-01-26")
        self.bar_canvas.show_bar_graph(totals,"2015-01-26")

    def set_pie_chart(self):
        self.stacked_layout.setCurrentIndex(1)

    def set_bar_chart(self):
        self.stacked_layout.setCurrentIndex(0)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    application.exec_()
