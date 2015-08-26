from PyQt4.QtGui import *
from PyQt4.QtCore import *
#from PyQt4.QtSql import *

from sqlconnection_class import *
from format_database_class import *
from add_reading_class import *
from edit_reading_class import *
from remove_reading_class import *
from add_user_class import *
from edit_user_class import *
from remove_user_class import *
from add_cost_class import *
from edit_cost_class import *
from delete_cost_class import *
from add_type_class import *
from edit_type_class import *
from delete_type_class import *
from table_layout_class_new import *
from reading_canvas_class import *
from graph_controller_class import *
from bar_widget_class import *
from pie_widget_class import *
from scatter_widget_class import *
from line_widget_class import *

import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consumption Metering System")

        self.database_open = True
        self.database = "ConsumptionMeteringSystem.db"

        self.main_layout = QStackedLayout()
        self.show_table()
        self.show_bar_chart()
        self.show_pie_chart()
        self.show_scatter_graph()
        self.show_line_graph()

        self.table_widget.open_database()
        self.table_widget.get_tables()
        self.table_widget.get_types()

        self.bar_widget.get_tables()
        self.bar_widget.update_bar_chart()

        self.pie_widget.get_tables()
        self.pie_widget.update_pie_chart()

        self.scatter_widget.update_scatter_graph()

        self.line_widget.get_tables()
        self.line_widget.update_line_graph()
        
        self.main_layout_widget = QWidget()
        self.main_layout_widget.setLayout(self.main_layout)

        self.menu_bar = QMenuBar()
        self.status_bar = QStatusBar()
        
        self.database_menu = self.menu_bar.addMenu("Database")
        self.profile_menu = self.menu_bar.addMenu("Profile")
        self.reading_menu = self.menu_bar.addMenu("Readings")
        self.preferences_menu = self.menu_bar.addMenu("Preferences")
        self.graphs_menu = self.menu_bar.addMenu("Graphs")

        self.open_database = self.database_menu.addAction("Open Database")
        self.close_database = self.database_menu.addAction("Close Database")
        self.format_database = self.database_menu.addAction("Format Database")

        self.new_profile = self.profile_menu.addAction("New Profile")
        self.edit_profile = self.profile_menu.addAction("Edit Profile")
        self.remove_profile = self.profile_menu.addAction("Remove Profile")
        self.logout = self.profile_menu.addAction("Logout")

        self.add_reading = self.reading_menu.addAction("Add Reading")
        self.edit_reading = self.reading_menu.addAction("Edit Reading")
        self.remove_reading = self.reading_menu.addAction("Remove Reading")

        self.cost_preferences = self.preferences_menu.addMenu("Costs")
        self.type_preferences = self.preferences_menu.addMenu("Types")

        self.add_cost = self.cost_preferences.addAction("Add Cost")
        self.edit_cost = self.cost_preferences.addAction("Edit Cost")
        self.remove_cost = self.cost_preferences.addAction("Remove Cost")

        self.add_type = self.type_preferences.addAction("Add Type")
        self.edit_type = self.type_preferences.addAction("Edit Type")
        self.remove_type = self.type_preferences.addAction("Remove Type")

        self.display_bar_chart = self.graphs_menu.addAction("Bar Chart")
        self.display_pie_chart = self.graphs_menu.addAction("Pie Chart")
        self.display_scatter_graph = self.graphs_menu.addAction("Scatter Graph")
        self.display_line_graph = self.graphs_menu.addAction("Line Graph")
        self.display_table = self.graphs_menu.addAction("Table")

        self.setMenuWidget(self.menu_bar)
        self.setStatusBar(self.status_bar)

        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)
        self.format_database.triggered.connect(self.clear_database)

        self.add_reading.triggered.connect(self.new_reading)
        self.edit_reading.triggered.connect(self.modify_reading)
        self.remove_reading.triggered.connect(self.clear_reading)

        self.new_profile.triggered.connect(self.new_user)
        self.edit_profile.triggered.connect(self.edit_user)
        self.remove_profile.triggered.connect(self.remove_user)

        self.add_cost.triggered.connect(self.insert_cost)
        self.edit_cost.triggered.connect(self.change_cost)
        self.remove_cost.triggered.connect(self.delete_cost)

        self.add_type.triggered.connect(self.insert_type)
        self.edit_type.triggered.connect(self.change_type)
        self.remove_type.triggered.connect(self.delete_type)

        self.display_table.triggered.connect(self.show_table)
        self.display_bar_chart.triggered.connect(self.show_bar_chart)
        self.display_pie_chart.triggered.connect(self.show_pie_chart)
        self.display_scatter_graph.triggered.connect(self.show_scatter_graph)
        self.display_line_graph.triggered.connect(self.show_line_graph)

        self.setCentralWidget(self.main_layout_widget)
        self.main_layout.setCurrentIndex(0)

    def open_connection(self):
        Path = QFileDialog.getOpenFileName(caption="Open Database")
        self.SQLConnection = SQLConnection(Path)
        ok = self.SQLConnection.open_database()
        if ok:
            self.database_open = True
            self.database = Path
            self.status_bar.showMessage("Database successfully opened")
            self.table_widget.get_tables()
            
            self.bar_widget.get_tables()
            self.bar_widget.update_bar_chart()

            self.pie_widget.get_tables()
            self.pie_widget.update_pie_chart()

            self.scatter_widget.update_scatter_graph()

            self.line_widget.get_tables()
            self.line_widget.update_line_graph()
         
        else:
            self.database_open = False
            self.status_bar.showMessage("Database failed to open")

    def close_connection(self):
        if self.database_open:
            self.SQLConnection.close_database()
            self.database = None
            self.database_open = False
            self.table_widget.select_table.clear()
            self.table_widget.select_type.clear()
        else:
            self.status_bar.showMessage("There is no database currently open")

    def clear_database(self):
        if self.database_open:
            self.format_database_window = FormatDatabase()
            self.format_database_window.show()
            self.format_database_window.raise_()
        else:
            self.status_bar.showMessage("There is no database currently open")

    def new_reading(self):
        if self.database_open:
            self.insert_reading = AddReading(self.database)
            self.insert_reading.show()
            self.insert_reading.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def modify_reading(self):
        if self.database_open:
            self.change_reading = EditReading(self.database)
            self.change_reading.show()
            self.change_reading.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def clear_reading(self):
        if self.database_open:
            self.delete_reading = RemoveReading(self.database)
            self.delete_reading.show()
            self.delete_reading.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def new_user(self):
        if self.database_open:
            self.new_user_window = NewProfile(self.database)
            self.new_user_window.show()
            self.new_user_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def edit_user(self):
        if self.database_open:
            self.edit_user_window = EditUser(self.database)
            self.edit_user_window.show()
            self.edit_user_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def remove_user(self):
        if self.database_open:
            self.remove_user_window = RemoveUser(self.database)
            self.remove_user_window.show()
            self.remove_user_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def insert_cost(self):
        if self.database_open:
            self.add_cost_window = AddCost(self.database)
            self.add_cost_window.show()
            self.add_cost_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def change_cost(self):
        if self.database_open:
            self.modify_cost_window = EditCost(self.database)
            self.modify_cost_window.show()
            self.modify_cost_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")        
    def delete_cost(self):
        if self.database_open:
            self.delete_cost_window = DeleteCost(self.database)
            self.delete_cost_window.show()
            self.delete_cost_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")
    def insert_type(self):
        if self.database_open:
            self.add_type_window = AddType(self.database)
            self.add_type_window.show()
            self.add_type_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")
    def change_type(self):
        if self.database_open:
            self.edit_type_window = EditType(self.database)
            self.edit_type_window.show()
            self.edit_type_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def delete_type(self):
        if self.database_open:
            self.remove_type_window = DeleteType(self.database)
            self.remove_type_window.show()
            self.remove_type_window.raise_()
        else:
            self.status_bar.showMessage("Database not open")

    def show_table(self):
        if not hasattr(self,"table_widget"):
            self.table_widget = DisplayTable(self.database)
            self.main_layout.addWidget(self.table_widget)
        else:
            self.main_layout.setCurrentIndex(0)
            

    def show_bar_chart(self):
        if not hasattr(self,"bar_widget"):
            self.bar_widget = BarWidget(self.database)
            self.main_layout.addWidget(self.bar_widget)
        else:
            self.main_layout.setCurrentIndex(1)

    def show_pie_chart(self):
        if not hasattr(self,"pie_widget"):
            self.pie_widget = PieWidget(self.database)
            self.main_layout.addWidget(self.pie_widget)
        else:
            self.main_layout.setCurrentIndex(2)

    def show_scatter_graph(self):
        if not hasattr(self,"scatter_widget"):
            self.scatter_widget = ScatterWidget(self.database)
            self.main_layout.addWidget(self.scatter_widget)
        else:
            self.main_layout.setCurrentIndex(3)

    def show_line_graph(self):
        if not hasattr(self,"line_widget"):
            self.line_widget = LineWidget(self.database)
            self.main_layout.addWidget(self.line_widget)
        else:
            self.main_layout.setCurrentIndex(4)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
