# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
# from tkinter import messagebox

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox




class Ui_SignupPage(object):
    def __init__(self,window):
        self.window=window
    #sign up buttton


    def loginaction(self):

        conn = sqlite3.connect("project")
        conn.execute('''create table IF NOT EXISTS users(id integer primary key AUTOINCREMENT,
                                                              email varchar(30) not null,
                                                              username varchar(50) not null,
                                                              password varchar(30) not null,
                                                              confirm_password varchar(30) not null)''')

        name = self.username_signup.text()
        email = self.useremail_signup.text()
        password = self.password_signup.text()
        cpassword = self.cpassword_signup.text()
        # result = conn.execute('select * from users where username = ? and password = ?', (name, password))
        if name=="":

            msg = QMessageBox()
            msg.setWindowTitle("Leaf Restaurant")
            msg.setText("Please fill in all the information")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif email == "":
            msg = QMessageBox()
            msg.setWindowTitle("Leaf Restaurant")
            msg.setText("Please fill in all the information")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif password == "":
            msg = QMessageBox()
            msg.setWindowTitle("Leaf Restaurant")
            msg.setText("Please fill in all the information")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif cpassword == "":
            msg = QMessageBox()
            msg.setWindowTitle("Leaf Restaurant")
            msg.setText("Please fill in all the information")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif password != cpassword:
            msg=QMessageBox()
            msg.setWindowTitle("Leaf Restaurant")
            msg.setText("Passwords Much Match!")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        #
        #
        # elif (len(result.fetchall()) > 0):
        #     msg = QMessageBox()
        #     msg.setWindowTitle("Warning!")
        #     msg.setText("The username already exists!")
        #     msg.setIcon(QMessageBox.Warning)
        #     x = msg.exec_()
        else:

            conn.execute("insert into users(email,username, password,confirm_password) values(?, ?, ?,?)",
                         (email, name, password, cpassword))
            conn.commit()

            self.openwindow()


        # messagebox.showinfo(title='Warning!',message='Passwords must match')
        # # print('Sorry')

        conn.close()
        ###Switch to the  login page

    def openwindow(self):
        self.window.close()
        from ui_folder.login import Ui_LoginPage
        self.window = QtWidgets.QDialog()
        self.ui = Ui_LoginPage(self.window)
        self.ui.setupUi(self.window)
        ###hides the previous window

        self.window.show()

    def setupUi(self, SignupPage):
        SignupPage.setObjectName("SignupPage")
        SignupPage.resize(651, 583)
        SignupPage.setStyleSheet("")
        self.Background = QtWidgets.QLabel(SignupPage)
        self.Background.setGeometry(QtCore.QRect(0, 0, 651, 581))
        self.Background.setStyleSheet("")
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("../images/b_su.png"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.useremail_signup = QtWidgets.QLineEdit(SignupPage)
        self.useremail_signup.setGeometry(QtCore.QRect(160, 200, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.useremail_signup.setFont(font)
        self.useremail_signup.setStyleSheet("background-color: white;\n"
"border: 3px solid #4DD0E1;\n"
"border-radius: 25px;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"font-color:gray;\n"
"")
        self.useremail_signup.setObjectName("useremail_signup")
        self.signupbtn = QtWidgets.QPushButton(SignupPage)
        self.signupbtn.setGeometry(QtCore.QRect(250, 450, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.signupbtn.setFont(font)
        self.signupbtn.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-color:gray;\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #EEEEEE;\n"
"border-style:inset;\n"
"color: #0097A7;\n"
"}\n"
"\n"
"")
        self.signupbtn.setObjectName("signupbtn")
        ####Action####
        self.signupbtn.clicked.connect(self.loginaction)
        ##############
        self.label = QtWidgets.QLabel(SignupPage)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 581))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/signup.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.password_signup = QtWidgets.QLineEdit(SignupPage)
        self.password_signup.setGeometry(QtCore.QRect(160, 320, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.password_signup.setFont(font)
        self.password_signup.setStyleSheet("background-color: white;\n"
"border: 3px solid #4DD0E1;\n"
"border-radius: 25px;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"font-color:gray;")
        self.password_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_signup.setObjectName("password_signup")
        self.label_2 = QtWidgets.QLabel(SignupPage)
        self.label_2.setGeometry(QtCore.QRect(260, 90, 101, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../images/person.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.username_signup = QtWidgets.QLineEdit(SignupPage)
        self.username_signup.setGeometry(QtCore.QRect(160, 260, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.username_signup.setFont(font)
        self.username_signup.setStyleSheet("background-color: white;\n"
"border: 3px solid #4DD0E1;\n"
"border-radius: 25px;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"font-color:gray;\n"
"")
        self.username_signup.setObjectName("username_signup")
        self.cpassword_signup = QtWidgets.QLineEdit(SignupPage)
        self.cpassword_signup.setGeometry(QtCore.QRect(160, 380, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cpassword_signup.setFont(font)
        self.cpassword_signup.setStyleSheet("background-color: white;\n"
"border: 3px solid #4DD0E1;\n"
"border-radius: 25px;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"font-color:gray;")
        self.cpassword_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpassword_signup.setObjectName("cpassword_signup")
        self.label.raise_()
        self.Background.raise_()
        self.useremail_signup.raise_()
        self.signupbtn.raise_()
        self.password_signup.raise_()
        self.label_2.raise_()
        self.username_signup.raise_()
        self.cpassword_signup.raise_()

        self.retranslateUi(SignupPage)
        QtCore.QMetaObject.connectSlotsByName(SignupPage)

    def retranslateUi(self, SignupPage):
        _translate = QtCore.QCoreApplication.translate
        SignupPage.setWindowTitle(_translate("SignupPage", "Dialog"))
        self.useremail_signup.setPlaceholderText(_translate("SignupPage", "Email Address"))
        self.signupbtn.setText(_translate("SignupPage", "Sign Up"))
        self.password_signup.setPlaceholderText(_translate("SignupPage", "Password"))
        self.username_signup.setPlaceholderText(_translate("SignupPage", "Username"))
        self.cpassword_signup.setPlaceholderText(_translate("SignupPage", "Confirm Password"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupPage = QtWidgets.QDialog()
    ui = Ui_SignupPage(SignupPage)
    ui.setupUi(SignupPage)
    SignupPage.show()
    sys.exit(app.exec_())