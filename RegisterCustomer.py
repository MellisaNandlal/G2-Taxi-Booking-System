from PyQt6.QtWidgets import QCheckBox
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QLabel, QMainWindow, QPushButton, QApplication, QLineEdit

import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        # changing the background color to yellow 
        self.setStyleSheet("background-color: yellow;")

        # set the title 
        self.setWindowTitle("Turbo Taxi Customer Registration")

        self.label = QLabel("Please fill out to Register", self)
        self.label.move(25, 25)
        self.label.setStyleSheet("""
        font-size: 15px
        """)

        # setting  the geometry of window 
        self.setGeometry(500, 200, 500, 550)

        # creating a label widget 
        self.label = QLabel("First Name : ", self)
        self.label.move(40, 60)
        self.label.setStyleSheet("""
        font-size: 15px
        """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 60)

        self.label = QLabel("Last Name : ", self)
        self.label.move(40, 90)
        self.label.setStyleSheet("""
        font-size: 15px
        """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 90)

        self.label = QLabel("Address : ", self)
        self.label.move(40, 120)
        self.label.setStyleSheet("""
        font-size: 15px
        """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 120)


        self.label = QLabel("Phone Number : ", self)
        self.label.move(40, 150)
        self.label.setStyleSheet("""
        font-size: 15px
        """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 150)

        self.label = QLabel("Email Address : ", self)
        self.label.move(40, 180)
        self.label.setStyleSheet("""
        font-size: 15px
        """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 180)


        self.label = QLabel("Password : ", self)
        self.label.move(40, 210)
        self.label.setStyleSheet("""
        font-size: 15px
        """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 210)

        self.label = QLabel("Confirm Password : ", self)
        self.label.move(40, 240)
        self.label.setStyleSheet("""
        font-size: 15px
        """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 240)

        self.label = QLabel("Payment Method : ", self)
        self.label.move(40, 270)
        self.label.setStyleSheet("""
        font-size: 15px
        """)

        self.label = QLabel("VISA ", self)
        self.label.move(80, 300)
        self.label.setStyleSheet("""
        font-size: 15px
        """)

        self.label = QLabel("MASTERCARD ", self)
        self.label.move(150, 300)
        self.label.setStyleSheet("""
        font-size: 15px
        """)

        self.label = QLabel("Credit Card Number ", self)
        self.label.move(40, 330)
        self.label.setStyleSheet("""
        font-size: 15px
        """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 330)

        self.label = QLabel("Expiry Date ", self)
        self.label.move(40, 360)
        self.label.setStyleSheet("""
                font-size: 15px
                """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 360)

        self.label = QLabel("CVC Code ", self)
        self.label.move(40, 390)
        self.label.setStyleSheet("""
                font-size: 15px
                """)
        self.userTextbox = QLineEdit(self)
        self.userTextbox.move(250, 390)

        #Do a checkbox here
        self.label = QLabel(" I agree to Terms & Conditions", self)
        self.label.move(80, 430)
        self.label.setStyleSheet("""
        font-size: 12px
        """)

        self.terms_checkbox = QCheckBox()
        self.terms_checkbox.move(80, 430)
        self.terms_checkbox.setStyleSheet("font-size: 12px")


        self.button = QPushButton("Register", self)
        #self.button.clicked.connect(self.button_clicked)
        self.button.move(100, 470)

        self.button = QPushButton("Cancel", self)
        # self.button.clicked.connect(self.button_clicked)
        self.button.move(250, 470)


        # show all the widgets
        self.show()

        def button_clicked(self):
           if self.terms_checkbox.isChecked():
               print("Registered Successfully!")
           else:
               print("Please agree to Terms & Conditions to register.")


app = QApplication(sys.argv)

# create the instance of our Window 


window = window()

window.show()


# start the app
sys.exit(app.exec())
