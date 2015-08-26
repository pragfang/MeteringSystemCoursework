from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Combo Box")

        self.layout = QVBoxLayout()

        self.combo_box = QComboBox()

        self.layout.addWidget(self.combo_box)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)

if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    Window.raise_()
    Application.exec_()
