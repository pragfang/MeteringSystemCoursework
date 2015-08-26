from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class RemoveData(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remove Data")
        
        self.icon = QIcon('./icon.png')
        self.setWindowIcon(self.icon)

        self.stacked_layout = QStackedLayout()
        self.create_remove_data_layout()
        self.create_confirm_layout()

        self.stacked_layout.addWidget(self.remove_data_widget)
        self.stacked_layout.addWidget(self.confirmation_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

    def create_remove_data_layout(self):
        if not hasattr(self,"remove_data_layout"):
            self.data_table_text = QLabel("Data table:")
            self.data_type_text = QLabel("Data type:")
            self.data_selection_text = QLabel("Data:")
            self.data_table_dropdown = QPushButton("None")
            self.data_type_dropdown = QPushButton("None")
            self.data_selection_dropdown = QPushButton("None")
            self.confirm_button = QPushButton("Confirm")
            self.back_button = QPushButton("Back")

            self.data_table_dropdown_menu = QMenu()
            self.data_type_dropdown_menu = QMenu()
            self.data_selection_dropdown_menu = QMenu()

            self.data_table_dropdown.setMenu(self.data_table_dropdown_menu)
            self.data_type_dropdown.setMenu(self.data_type_dropdown_menu)
            self.data_selection_dropdown.setMenu(self.data_selection_dropdown_menu)

            self.data_table_layout = QHBoxLayout()
            self.data_table_layout.addWidget(self.data_table_text)
            self.data_table_layout.addWidget(self.data_table_dropdown)

            self.data_type_layout = QHBoxLayout()
            self.data_type_layout.addWidget(self.data_type_text)
            self.data_type_layout.addWidget(self.data_type_dropdown)

            self.data_selection_layout = QHBoxLayout()
            self.data_selection_layout.addWidget(self.data_selection_text)
            self.data_selection_layout.addWidget(self.data_selection_dropdown)

            self.confirm_button_layout = QHBoxLayout()
            self.confirm_button_layout.addWidget(self.confirm_button)
            self.confirm_button_layout.addWidget(self.back_button)

            self.remove_data_layout = QVBoxLayout()
            self.remove_data_layout.addLayout(self.data_table_layout)
            self.remove_data_layout.addLayout(self.data_type_layout)
            self.remove_data_layout.addLayout(self.data_selection_layout)
            self.remove_data_layout.addLayout(self.confirm_button_layout)
            
            self.remove_data_widget = QWidget()
            self.remove_data_widget.setLayout(self.remove_data_layout)

            self.confirm_button.clicked.connect(self.create_confirm_layout)
            self.back_button.clicked.connect(self.close)

        else:
            self.stacked_layout.setCurrentIndex(0)

    def create_confirm_layout(self):
        if not hasattr(self,"confirmation_layout"):
            self.warning = QLabel("Are you sure you want to delete this data:")
            self.data = QLabel("-data-")
            self.yes_button = QPushButton("Yes")
            self.no_button = QPushButton("No")

            self.warning_layout = QVBoxLayout()
            self.warning_layout.addWidget(self.warning)
            self.warning_layout.addWidget(self.data)

            self.yesno_button_layout = QHBoxLayout()
            self.yesno_button_layout.addWidget(self.yes_button)
            self.yesno_button_layout.addWidget(self.no_button)

            self.confirmation_layout = QVBoxLayout()
            self.confirmation_layout.addLayout(self.warning_layout)
            self.confirmation_layout.addLayout(self.yesno_button_layout)

            self.confirmation_widget = QWidget()
            self.confirmation_widget.setLayout(self.confirmation_layout)

            self.no_button.clicked.connect(self.create_remove_data_layout)
            self.yes_button.clicked.connect(self.remove_data)
        else:
            self.stacked_layout.setCurrentIndex(1)

    def remove_data(self):
        pass

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = RemoveData()
    window.show()
    window.raise_()
    application.exec_()
