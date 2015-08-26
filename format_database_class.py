from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class FormatDatabase(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Format Database")

        self.create_format_database_layout()
        self.setCentralWidget(self.format_database_widget)

    def create_format_database_layout(self):
        self.warning = QLabel("Are you sure you want to format the database?")
        self.yes_button = QPushButton("Yes")
        self.no_button = QPushButton("No")

        self.yesno_button_layout = QHBoxLayout()
        self.yesno_button_layout.addWidget(self.yes_button)
        self.yesno_button_layout.addWidget(self.no_button)

        self.format_database_layout = QVBoxLayout()
        self.format_database_layout.addWidget(self.warning)
        self.format_database_layout.addLayout(self.yesno_button_layout)

        self.format_database_widget = QWidget()
        self.format_database_widget.setLayout(self.format_database_layout)

        self.yes_button.clicked.connect(self.format_database)
        self.no_button.clicked.connect(self.close)

    def format_database(self):
        pass

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = FormatDatabase()
    window.show()
    window.raise_()
    application.exec_()
