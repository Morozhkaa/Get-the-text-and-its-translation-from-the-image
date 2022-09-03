# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GetText(object):
    def setupUi(self, GetText):
        GetText.setObjectName("GetText")
        GetText.resize(975, 756)
        GetText.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(229, 133, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(152, 76, 178, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.centralwidget = QtWidgets.QWidget(GetText)
        self.centralwidget.setObjectName("centralwidget")
        self.AddPicture = QtWidgets.QPushButton(self.centralwidget)
        self.AddPicture.setGeometry(QtCore.QRect(220, 650, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AddPicture.setFont(font)
        self.AddPicture.setStyleSheet("background-color: rgb(200, 60, 255);\n"
"color: rgb(0, 0, 0);")
        self.AddPicture.setCheckable(False)
        self.AddPicture.setDefault(True)
        self.AddPicture.setObjectName("AddPicture")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-10, -70, 1031, 901))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.background.setFont(font)
        self.background.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("1.jpg"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QTextBrowser(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 561, 331))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 650, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 164, 119);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 650, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(220, 350, 561, 281))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.background.raise_()
        self.AddPicture.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.textBrowser.raise_()
        GetText.setCentralWidget(self.centralwidget)

        self.retranslateUi(GetText)
        QtCore.QMetaObject.connectSlotsByName(GetText)

    def retranslateUi(self, GetText):
        _translate = QtCore.QCoreApplication.translate
        GetText.setWindowTitle(_translate("GetText", "GetTextFromPicture"))
        self.AddPicture.setText(_translate("GetText", "Add picture"))
        self.pushButton.setText(_translate("GetText", "Paste from clipboard"))
        self.pushButton_2.setText(_translate("GetText", "Copy"))
