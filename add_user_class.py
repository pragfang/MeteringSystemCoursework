from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3

class NewProfile(QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database

        self.setWindowTitle("New Profile")

        self.create_new_user_layout()
        self.setCentralWidget(self.new_user_widget)

    def create_new_user_layout(self):
        self.first_name_label = QLabel("First Name:")
        self.first_name_input = QLineEdit()
        
        self.last_name_label = QLabel("Last Name:")
        self.last_name_input = QLineEdit()
        
        self.password_label = QLabel("Password: ")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(2)

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.first_name_layout = QHBoxLayout()
        self.first_name_layout.addWidget(self.first_name_label)
        self.first_name_layout.addWidget(self.first_name_input)

        self.last_name_layout = QHBoxLayout()
        self.last_name_layout.addWidget(self.last_name_label)
        self.last_name_layout.addWidget(self.last_name_input)

        self.password_layout = QHBoxLayout()
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.new_user_layout = QVBoxLayout()
        self.new_user_layout.addLayout(self.first_name_layout)
        self.new_user_layout.addLayout(self.last_name_layout)
        self.new_user_layout.addLayout(self.password_layout)
        self.new_user_layout.addLayout(self.button_layout)

        self.new_user_widget = QWidget()
        self.new_user_widget.setLayout(self.new_user_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.add_user)

    def add_user(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        password = self.password_input.text()

        sql = "INSERT INTO User(FirstName,LastName,UserPassword) VALUES(?,?,?)"
        data = [first_name,last_name,password]
        self.query(data,sql)
        self.close()

    def query(self,data,sql):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()
