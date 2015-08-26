from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import*

from home_layout_class import *
from bar_layout_class import *
from sqlconnection_class import *
from add_data_class import *
from remove_data_class import *
from format_database_class import *
from edit_data_class import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consumption Metering System")

        self.icon = QIcon("./icon.png")
        self.setWindowIcon(self.icon)

        self.database_open = True
        self.database = "ConsumptionMeteringSystem.db"

        self.tabs = QTabWidget()
        self.menu_bar = QMenuBar()
        self.status_bar = QStatusBar()

        self.database_menu = self.menu_bar.addMenu("Database")
        self.open_database = self.database_menu.addAction("Open Database")
        self.close_database = self.database_menu.addAction("Close Database")
        self.create_database = self.database_menu.addAction("Create Database")
        self.format_database = self.database_menu.addAction("Format Database")
        self.add_data = self.database_menu.addAction("Add Data")
        self.remove_data = self.database_menu.addAction("Remove Data")
        self.edit_data = self.database_menu.addAction("Edit Data")

        self.setMenuWidget(self.menu_bar)
        self.setStatusBar(self.status_bar)

        self.home_tab = QWidget()
        self.bar_tab = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()

        self.create_home_layout()
        self.create_bar_layout()

        self.tabs.addTab(self.home_tab, "Home")
        self.tabs.addTab(self.bar_tab, "Bar Chart")
        self.tabs.addTab(self.tab3, "Graph 2")
        self.tabs.addTab(self.tab4, "Graph 3")
        self.tabs.addTab(self.tab5, "Graph 4")
        self.tabs.addTab(self.tab6, "Graph 5")
        self.tabs.addTab(self.tab7, "Graph 6")
        self.tabs.addTab(self.tab8, "Graph 7")

        self.tabs.setTabShape(QTabWidget.Rounded)

        self.setCentralWidget(self.tabs)

        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)
        self.create_database.triggered.connect(self.new_database)
        self.format_database.triggered.connect(self.clear_database)
        self.add_data.triggered.connect(self.insert_data)
        self.remove_data.triggered.connect(self.delete_data)
        self.edit_data.triggered.connect(self.change_data)

    def create_home_layout(self):
        if not hasattr(self,"home_layout"):
            self.home_layout = HomeLayout(self.database_open,self.database)
            self.home_tab.setLayout(self.home_layout)
            
    def create_bar_layout(self):
        if not hasattr(self,"bar_layout"):
            self.bar_layout = CreateBarLayout()
            self.bar_tab.setLayout(self.bar_layout)

    def open_connection(self):
        self.status_bar.showMessage("Opening Database")
        Path = QFileDialog.getOpenFileName()
        self.SQLConnection = SQLConnection(Path)
        ok = self.SQLConnection.open_database()
        if ok:
            self.status_bar.showMessage("Database opened successfully")
            self.database_open = True
            self.database = Path
            self.home_layout.tool_bar.database_open = self.database_open
            self.home_layout.tool_bar.database = database
        else:
            self.status_bar.showMessage("Database failed to open")
            self.database_open = False

    def close_connection(self):
        if self.database_open == True:
            self.SQLConnection.close_database()
            self.status_bar.showMessage("Database closed successfully")
            self.database_open = False
        else:
            self.status_bar.showMessage("There is no database currently open")

    def new_database(self):
        pass

    def clear_database(self):
        if self.database_open == True:
            if not hasattr(self,"FormatDatabase"):
                self.FormatDatabase = FormatDatabase()
            self.FormatDatabase.show()
            self.FormatDatabase.raise_()
        else:
            self.status_bar.showMessage("There is no database currently open")

    def insert_data(self):
        if self.database_open == True:
            if not hasattr(self,"AddData"):
                self.AddData = AddData(self.database)
            self.AddData.show()
            self.AddData.raise_()
        else:
            self.status_bar.showMessage("There is no database currently open")

    def delete_data(self):
        if self.database_open == True:
            if not hasattr(self,"RemoveData"):
                self.RemoveData = RemoveData()
                self.RemoveData.show()
                self.RemoveData.raise_()
        else:
            self.status_bar.showMessage("There is no database currently open")

    def change_data(self):
        if self.database_open == True:
            if not hasattr(self,"EditData"):
                self.EditData = EditData(self.database)
            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

        
