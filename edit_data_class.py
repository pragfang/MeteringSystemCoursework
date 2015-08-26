from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class EditData(QMainWindow):
    def __init__(self,db):
        super().__init__()
        self.setWindowTitle("Edit Data")
        self.stacked_layout = QStackedLayout()

        self.database = db

        self.create_data_selection_layout()
        self.create_edit_data_layout()
        self.create_confirmation_layout()
        self.edit_data_a
        self.edit_data_b

        self.stacked_layout.addWidget(self.data_selection_widget)
        self.stacked_layout.addWidget(self.edit_data_widget)
        self.stacked_layout.addWidget(self.confirmation_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

    def create_data_selection_layout(self):
        if not hasattr(self,"data_selection_layout"):
            self.data_table = QLabel("Data Table:")
            self.data_type = QLabel("Data Type:")
            self.data = QLabel("Data:")
            self.data_table_dropdown = QPushButton("None")
            self.data_type_dropdown = QPushButton("None")
            self.data_dropdown = QPushButton("None")
            self.proceed_button = QPushButton("Proceed")
            self.back_button_a = QPushButton("Back")

            self.data_table_menu = QMenu()
            self.data_type_menu = QMenu()
            self.data_menu = QMenu()
            self.data_table_dropdown.setMenu(self.data_table_menu)
            self.data_type_dropdown.setMenu(self.data_type_menu)
            self.data_dropdown.setMenu(self.data_menu)

            self.data_table_layout = QHBoxLayout()
            self.data_table_layout.addWidget(self.data_table)
            self.data_table_layout.addWidget(self.data_table_dropdown)

            self.data_type_layout = QHBoxLayout()
            self.data_type_layout.addWidget(self.data_type)
            self.data_type_layout.addWidget(self.data_type_dropdown)

            self.data_layout = QHBoxLayout()
            self.data_layout.addWidget(self.data)
            self.data_layout.addWidget(self.data_dropdown)

            self.button_layout_a = QHBoxLayout()
            self.button_layout_a.addWidget(self.proceed_button)
            self.button_layout_a.addWidget(self.back_button_a)

            self.data_selection_layout = QVBoxLayout()
            self.data_selection_layout.addLayout(self.data_table_layout)
            self.data_selection_layout.addLayout(self.data_type_layout)
            self.data_selection_layout.addLayout(self.data_layout)
            self.data_selection_layout.addLayout(self.button_layout_a)
            
            self.data_selection_widget = QWidget()
            self.data_selection_widget.setLayout(self.data_selection_layout)

            self.proceed_button.clicked.connect(self.create_edit_data_layout)
            self.back_button_a.clicked.connect(self.close)
        else:
            self.stacked_layout.setCurrentIndex(0)

    def create_edit_data_layout(self):
        if not hasattr(self,"edit_data_layout"):
            self.data_name_a = QLabel()
            self.data_name_b = QLabel()
            self.data_line_a = QLabel()
            self.data_line_b = QLabel()
            self.edit_line_a = QPushButton("Edit")
            self.edit_line_b = QPushButton("Edit")
            self.confirm_button_a = QPushButton("Confirm")
            self.back_button_b = QPushButton("Back")

            self.data_line_a_layout = QHBoxLayout()
            self.data_line_a_layout.addWidget(self.data_name_a)
            self.data_line_a_layout.addWidget(self.data_line_a)
            self.data_line_a_layout.addWidget(self.edit_line_a)

            self.data_line_b_layout = QHBoxLayout()
            self.data_line_b_layout.addWidget(self.data_name_b)
            self.data_line_b_layout.addWidget(self.data_line_b)
            self.data_line_b_layout.addWidget(self.edit_line_b)

            self.button_layout_b = QHBoxLayout()
            self.button_layout_b.addWidget(self.confirm_button_a)
            self.button_layout_b.addWidget(self.back_button_b)

            self.edit_data_layout = QVBoxLayout()
            self.edit_data_layout.addLayout(self.data_line_a_layout)
            self.edit_data_layout.addLayout(self.data_line_b_layout)
            self.edit_data_layout.addLayout(self.button_layout_b)
            
            self.edit_data_widget = QWidget()
            self.edit_data_widget.setLayout(self.edit_data_layout)

            self.edit_line_a.clicked.connect(self.edit_data_a)
            self.edit_line_b.clicked.connect(self.edit_data_b)
            self.confirm_button_a.clicked.connect(self.create_confirmation_layout)
            self.back_button_b.clicked.connect(self.create_data_selection_layout)
        else:
            self.stacked_layout.setCurrentIndex(1)

    def create_confirmation_layout(self):
        if not hasattr(self,"confirmation_layout"):
            self.confirm_button_b = QPushButton("Confirm")
            self.back_button_c = QPushButton("Back")

            self.button_layout_c = QHBoxLayout()
            self.button_layout_c.addWidget(self.confirm_button_b)
            self.button_layout_c.addWidget(self.back_button_c)

            self.confirmation_layout = QVBoxLayout()
            self.confirmation_layout.addLayout(self.button_layout_c)

            self.confirmation_widget = QWidget()
            self.confirmation_widget.setLayout(self.confirmation_layout)

            self.confirm_button_b.clicked.connect(self.edit_data)
            self.back_button_c.clicked.connect(self.create_edit_data_layout)
        else:
            self.stacked_layout.setCurrentIndex(2)

    def edit_data_a(self):
        if not hasattr(self,"edit_line_a_layout"):
            self.current_data_a = QLabel("Current Data:")
            self.new_data_a =  QLabel("New Data:")
            self.new_data_edit_a = QLineEdit()
            self.confirm_button_c = QPushButton("Confirm")
            self.back_button_d = QPushButton("Back")

            self.new_data_layout_a = QGridLayout()
            self.new_data_layout_a.addWidget(self.current_data_a,1,1)
            self.new_data_layout_a.addWidget(self.new_data_a,2,1)
            self.new_data_layout_a.addWidget(self.data_line_a,1,2)
            self.new_data_layout_a.addWidget(self.new_data_edit_a,2,2)

            self.button_layout_d = QHBoxLayout()
            self.button_layout_d.addWidget(self.confirm_button_c)
            self.button_layout_d.addWidget(self.back_button_d)

            self.edit_line_a_layout = QVBoxLayout()
            self.edit_line_a_layout.addLayout(self.new_data_layout_a)
            self.edit_line_a_layout.addLayout(self.button_layout_d)

            self.edit_line_a_widget = QWidget()
            self.edit_line_a_widget.setLayout(self.edit_line_a_layout)

            self.stacked_layout.addWidget(self.edit_line_a_widget)

            self.back_button_d.clicked.connect(self.create_edit_data_layout)
        self.stacked_layout.setCurrentIndex(3)
        
    def edit_data_b(self):
        if not hasattr(self,"edit_line_a_layout"):
            self.current_data_b = QLabel("Current Data:")
            self.new_data_b =  QLabel("New Data:")
            self.new_data_edit_b = QLineEdit()
            self.confirm_button_c = QPushButton("Confirm")
            self.back_button_d = QPushButton("Back")

            self.new_data_layout_b = QGridLayout()
            self.new_data_layout_b.addWidget(self.current_data_b,1,1)
            self.new_data_layout_b.addWidget(self.new_data_b,2,1)
            self.new_data_layout_b.addWidget(self.data_line_b,1,2)
            self.new_data_layout_b.addWidget(self.new_data_edit_b,2,2)

            self.button_layout_e = QHBoxLayout()
            self.button_layout_e.addWidget(self.confirm_button_d)
            self.button_layout_e.addWidget(self.back_button_e)

            self.edit_line_b_layout = QVBoxLayout()
            self.edit_line_b_layout.addLayout(self.new_data_layout_b)
            self.edit_line_b_layout.addLayout(self.button_layout_e)

            self.edit_line_b_widget = QWidget()
            self.edit_line_b_widget.setLayout(self.edit_line_b_layout)

            self.stacked_layout.addWidget(self.edit_line_b_widget)

            self.back_button_e.clicked.connect(self.create_edit_data_layout)
        self.stacked_layout.setCurrentIndex(4)

    def edit_data(self):
        pass

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = EditData()    
    window.show()
    window.raise_()
    application.exec_()
