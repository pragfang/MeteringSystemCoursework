from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sqlite3

class RemoveUser(QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database
        
        self.setWindowTitle("Remove User")

        self.create_remove_user_layout()
        self.setCentralWidget(self.remove_user_widget)

    def create_remove_user_layout(self):
        self.user_label = QLabel("Select User:")
        self.select_user = QComboBox()

        self.get_users()

        self.back_button = QPushButton("Back")
        self.confirm_button = QPushButton("Confirm")

        self.select_user_layout = QHBoxLayout()
        self.select_user_layout.addWidget(self.user_label)
        self.select_user_layout.addWidget(self.select_user)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.confirm_button)

        self.remove_user_layout = QVBoxLayout()
        self.remove_user_layout.addLayout(self.select_user_layout)
        self.remove_user_layout.addLayout(self.button_layout)

        self.remove_user_widget = QWidget()
        self.remove_user_widget.setLayout(self.remove_user_layout)

        self.back_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.remove_user)

    def get_users(self):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("SELECT UserID,FirstName FROM User")
            users = cursor.fetchall()
        self.select_user.clear()
        for user in users:
            self.select_user.addItem("{0}. {1}".format(user[0],user[1]))

    def remove_user(self):
        user = self.select_user.currentText()
        
        sql = "DELETE FROM User WHERE UserID = ?"
        self.query(sql,user[0])
        self.close()

    def query(self,sql,user):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA Foreign_Keys = ON")
            cursor.execute(sql,user)
            db.commit()
