from PyQt4.QtGui import *

class AddElectricReading(QDialog):
    def __init__(self):
        super().__init__()

        self.create_add_electric_layout()

        self.setLayout(self.add_electric_layout)

    def create_add_electric_layout(self):
        self.reading_label = QLabel("Consumption Reading:")
        self.reading_input = QLineEdit()

        self.date_label = QLabel("Reading Date:")
        self.date_input = QLineEdit()

        self.confirm_button = QPushButton("Confirm")

        self.add_reading_layout = QGridLayout()
        self.add_reading_layout.addWidget(self.reading_label,1,1)
        self.add_reading_layout.addWidget(self.reading_input,2,1)
        self.add_reading_layout.addWidget(self.date_label,1,2)
        self.add_reading_layout.addWidget(self.date_input,2,2)

        self.add_electric_layout = QVBoxLayout()
        self.add_electric_layout.addLayout(self.add_reading_layout)
        self.add_electric_layout.addWidget(self.confirm_button)

        self.confirm_button.clicked.connect(self.add_data)

    def add_data(self):
        pass
