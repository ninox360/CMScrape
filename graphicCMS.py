# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphicCMS.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 132)
        MainWindow.setStyleSheet("background-color: rgb(28, 39, 40);\n"
"color: rgb(231, 231, 231);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputBtn = QtWidgets.QPushButton(self.centralwidget)
        self.inputBtn.setMinimumSize(QtCore.QSize(131, 23))
        self.inputBtn.setObjectName("inputBtn")
        self.verticalLayout.addWidget(self.inputBtn)
        self.statBtn = QtWidgets.QPushButton(self.centralwidget)
        self.statBtn.setMinimumSize(QtCore.QSize(131, 23))
        self.statBtn.setObjectName("statBtn")
        self.verticalLayout.addWidget(self.statBtn)
        self.outputBtn = QtWidgets.QPushButton(self.centralwidget)
        self.outputBtn.setMinimumSize(QtCore.QSize(131, 23))
        self.outputBtn.setObjectName("outputBtn")
        self.verticalLayout.addWidget(self.outputBtn)
        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setMinimumSize(QtCore.QSize(131, 23))
        self.runBtn.setObjectName("runBtn")
        self.verticalLayout.addWidget(self.runBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chosenFileLbl = QtWidgets.QLabel(self.centralwidget)
        self.chosenFileLbl.setMinimumSize(QtCore.QSize(200, 23))
        self.chosenFileLbl.setStyleSheet("color: rgb(156, 156, 156);\n"
"background-color: rgb(61, 61, 61);\n"
"border-color: rgb(71, 71, 71);")
        self.chosenFileLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.chosenFileLbl.setObjectName("chosenFileLbl")
        self.verticalLayout_2.addWidget(self.chosenFileLbl)
        self.chosenStatLbl = QtWidgets.QLabel(self.centralwidget)
        self.chosenStatLbl.setMinimumSize(QtCore.QSize(200, 23))
        self.chosenStatLbl.setStyleSheet("color: rgb(156, 156, 156);\n"
"background-color: rgb(61, 61, 61);\n"
"border-color: rgb(71, 71, 71);")
        self.chosenStatLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.chosenStatLbl.setObjectName("chosenStatLbl")
        self.verticalLayout_2.addWidget(self.chosenStatLbl)
        self.chosenOutLbl = QtWidgets.QLabel(self.centralwidget)
        self.chosenOutLbl.setMinimumSize(QtCore.QSize(200, 23))
        self.chosenOutLbl.setStyleSheet("color: rgb(156, 156, 156);\n"
"background-color: rgb(61, 61, 61);\n"
"border-color: rgb(71, 71, 71);\n"
"")
        self.chosenOutLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.chosenOutLbl.setObjectName("chosenOutLbl")
        self.verticalLayout_2.addWidget(self.chosenOutLbl)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(200, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid rgb(139, 28, 59);\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(172, 35, 72);\n"
"    width: 10px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.consoleLayout = QtWidgets.QVBoxLayout()
        self.consoleLayout.setObjectName("consoleLayout")
        self.consoleLbl = QtWidgets.QLabel(self.centralwidget)
        self.consoleLbl.setMinimumSize(QtCore.QSize(101, 16))
        self.consoleLbl.setStyleSheet("background-color: rgb(47, 66, 68);\n"
"color: rgb(231, 231, 231);\n"
"border-color: rgb(47, 47, 47);")
        self.consoleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.consoleLbl.setObjectName("consoleLbl")
        self.consoleLayout.addWidget(self.consoleLbl)
        self.consoleDisp = QtWidgets.QTextEdit(self.centralwidget)
        self.consoleDisp.setMinimumSize(QtCore.QSize(339, 113))
        self.consoleDisp.setSizeIncrement(QtCore.QSize(3, 1))
        self.consoleDisp.setStyleSheet("color: rgb(38, 209, 0);\n"
"border-color: rgb(71, 71, 71);\n"
"background-color: rgb(0, 0, 0);")
        self.consoleDisp.setReadOnly(True)
        self.consoleDisp.setObjectName("consoleDisp")
        self.consoleLayout.addWidget(self.consoleDisp)
        self.gridLayout.addLayout(self.consoleLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionHello = QtWidgets.QAction(MainWindow)
        self.actionHello.setObjectName("actionHello")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CMScrape - CardMarket Price Tracker"))
        self.inputBtn.setText(_translate("MainWindow", "Chose Input File"))
        self.statBtn.setText(_translate("MainWindow", "Chose Statistics File"))
        self.outputBtn.setText(_translate("MainWindow", "Chose Output File"))
        self.runBtn.setText(_translate("MainWindow", "Run"))
        self.chosenFileLbl.setText(_translate("MainWindow", "No file chosen"))
        self.chosenStatLbl.setText(_translate("MainWindow", "No file chosen"))
        self.chosenOutLbl.setText(_translate("MainWindow", "No file chosen"))
        self.actionHello.setText(_translate("MainWindow", "Hello"))
        self.consoleLbl.setText(_translate("MainWindow", "Console output :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ## What should be done is putting only the \r'd text in the console, rewriting it, and append the errors I could
    # ## in the begining or end of string, to be shown if user wants to.
    # ## maybe yet another argument "-se, --show-errors" that would work in cmd and
    MainWindow.show()
    sys.exit(app.exec_())
