# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 500)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 170, 255);\n"
"color: rgb(103, 92, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.educhart = QtWidgets.QLabel(self.centralwidget)
        self.educhart.setGeometry(QtCore.QRect(100, 50, 250, 50))
        self.educhart.setMinimumSize(QtCore.QSize(5, 1))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.educhart.setFont(font)
        self.educhart.setStyleSheet("\n"
"color: rgb(14, 18, 255);")
        self.educhart.setObjectName("educhart")
        self.teacher = QtWidgets.QPushButton(self.centralwidget)
        self.teacher.setGeometry(QtCore.QRect(140, 140, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.teacher.setFont(font)
        self.teacher.setStyleSheet("\n"
"background-color: rgb(220, 255, 254);")
        self.teacher.setObjectName("teacher")
        self.signin = QtWidgets.QPushButton(self.centralwidget)
        self.signin.setGeometry(QtCore.QRect(120, 330, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(20)
        self.signin.setFont(font)
        self.signin.setStyleSheet("color: rgb(255, 85, 0);")
        self.signin.setObjectName("signin")
        self.student = QtWidgets.QPushButton(self.centralwidget)
        self.student.setGeometry(QtCore.QRect(140, 210, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.student.setFont(font)
        self.student.setStyleSheet("background-color: rgb(210, 252, 255);")
        self.student.setObjectName("student")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EduChart-Sign in"))
        self.educhart.setText(_translate("MainWindow", "EduChart"))
        self.teacher.setText(_translate("MainWindow", "Teacher"))
        self.signin.setText(_translate("MainWindow", "Sign in"))
        self.student.setText(_translate("MainWindow", "Student"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
