from PyQt4.QtGui import *
from PyQt4.QtCore import *

from home_tool_bar_class import *
from add_data_widget_class import *

class HomeLayout(QStackedLayout):
    def __init__(self,database_open,database):
        super().__init__()
        self.tool_bar = HomeToolBar(database_open,database)
        self.create_home_layout()
        #self.add_data_widget = AddDataWidget(database)

        self.addWidget(self.home_widget)
        #self.addWidget(self.add_data_widget)

        self.setCurrentIndex(0)

    def create_home_layout(self):
        self.home_layout = QVBoxLayout()

        self.first_name_label = QLabel("First Name:")
        self.first_name = QLabel("-First Name-")
        self.last_name_label = QLabel("Last Name:")
        self.last_name = QLabel("-Last Name-")
        self.change_user = QPushButton("Change User")

        self.user_layout = QGridLayout()
        self.user_layout.addWidget(self.first_name_label,1,1)
        self.user_layout.addWidget(self.first_name,1,2)
        self.user_layout.addWidget(self.last_name_label,2,1)
        self.user_layout.addWidget(self.last_name,2,2)
        
        self.home_layout.addWidget(self.tool_bar)
        self.home_layout.addLayout(self.user_layout)
        self.home_layout.addWidget(self.change_user)

        self.home_widget = QWidget()
        self.home_widget.setLayout(self.home_layout)

if __name__ == "__main__":
    test = HomeLayout(True,"ConsumptionMeteringSystem.db")
    print(test)
