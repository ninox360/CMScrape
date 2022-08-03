# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphicCMS.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

DialogStyleSheet = "background-color: rgb(45, 45, 45);\n""color: rgb(211, 211, 211);\n""font: 11pt \"Ubuntu Mono\";""font-weight: bold"
TableViewStyleSheet = "background-color: rgb(70, 70, 70);\n"
GreenButtonStyleSheet = "background-color: rgb(71, 141, 75);\n""color: rgb(45, 45, 45);\n""border-color: rgb(0, 80, 0);"
RedButtonStyleSheet = "background-color: rgb(170, 16, 16);\n""color: rgb(45, 45, 45);\n""border-color: rgb(80, 0, 0);"
BlueButtonStyleSheet = "background-color: rgb(77, 84, 176);\n""color: rgb(45, 45, 45);\n""border-color: rgb(0, 0, 80);"
#NormalButtonStyleSheet =

_MAXVALUE_ = 999999999
SCREEN_HEIGHT = 0
SCREEN_WIDTH = 0

PreferenceLblMinSize = QtCore.QSize(int(SCREEN_WIDTH/5.8), 20)
PreferenceSpinBoxMinSize = QtCore.QSize(int(SCREEN_WIDTH/5.8), 20)

class UI_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(int(SCREEN_WIDTH/2.7), int(SCREEN_HEIGHT/4.8))
        Preferences.setFixedSize(int(SCREEN_WIDTH/2.7), int(SCREEN_HEIGHT/3.5))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        Preferences.setSizePolicy(sizePolicy)

        self.verticalLayout = QtWidgets.QVBoxLayout(Preferences)
        self.verticalLayout.setObjectName("verticalLayout")

        # Title
        self.gridLayoutTi = QtWidgets.QGridLayout()
        self.gridLayoutTi.setObjectName('gridLayoutTi')
        self.inTitle1 = QtWidgets.QLabel(Preferences)
        self.inTitle1.setMinimumSize(PreferenceLblMinSize)
        self.inTitle1.setBaseSize(PreferenceLblMinSize)
        self.inTitle1.setObjectName("inTitle1")
        self.gridLayoutTi.addWidget(self.inTitle1, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayoutTi)

        ## Number of Threads in scraping
        self.gridLayout3 = QtWidgets.QGridLayout()
        self.gridLayout3.setObjectName('gridLayout3')
        self.nThreadsLbl = QtWidgets.QLabel(Preferences)
        self.nThreadsLbl.setMinimumSize(PreferenceLblMinSize)
        self.nThreadsLbl.setObjectName('nThreadsLbl')
        self.gridLayout3.addWidget(self.nThreadsLbl, 0, 0, 1, 1)
        self.nThreads = QtWidgets.QSpinBox(Preferences)
        self.nThreads.setMinimumSize(PreferenceSpinBoxMinSize)
        self.nThreads.setBaseSize(PreferenceSpinBoxMinSize)
        self.nThreads.setObjectName('nThreads')
        self.nThreads.setMaximum(_MAXVALUE_)
        self.gridLayout3.addWidget(self.nThreads, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout3)
        
        ## Number of Threads in proxyChecking
        self.gridLayoutTproxyCheck = QtWidgets.QGridLayout()
        self.gridLayoutTproxyCheck.setObjectName('gridLayoutTproxyCheck')

        self.nProxyThreadsLbl = QtWidgets.QLabel(Preferences)
        self.nProxyThreadsLbl.setMinimumSize(PreferenceLblMinSize)
        self.nProxyThreadsLbl.setObjectName('nProxyThreadsLbl')
        self.gridLayoutTproxyCheck.addWidget(self.nProxyThreadsLbl, 0, 0, 1, 1)

        self.nProxyThreads = QtWidgets.QSpinBox(Preferences)
        self.nProxyThreads.setMinimumSize(PreferenceSpinBoxMinSize)
        self.nProxyThreads.setBaseSize(PreferenceSpinBoxMinSize)
        self.nProxyThreads.setObjectName('nProxyThreads')
        self.gridLayoutTproxyCheck.addWidget(self.nProxyThreads, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayoutTproxyCheck)

        ## Number of Proxies needed
        self.gridLayoutnProxyNeeded = QtWidgets.QGridLayout()
        self.gridLayoutnProxyNeeded.setObjectName('gridLayoutnProxyNeeded')

        self.nProxyLbl = QtWidgets.QLabel(Preferences)
        self.nProxyLbl.setMinimumSize(PreferenceLblMinSize)
        self.nProxyLbl.setObjectName('nProxyLbl')
        self.gridLayoutnProxyNeeded.addWidget(self.nProxyLbl, 0, 0, 1, 1)

        self.nProxy = QtWidgets.QSpinBox(Preferences)
        self.nProxy.setMinimumSize(PreferenceSpinBoxMinSize)
        self.nProxy.setBaseSize(PreferenceSpinBoxMinSize)
        self.nProxy.setObjectName('nProxy')
        self.gridLayoutnProxyNeeded.addWidget(self.nProxy, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayoutnProxyNeeded)

        ## Using a proxyFile
        self.gridLayoutUseProxyFile = QtWidgets.QGridLayout()
        self.gridLayoutUseProxyFile.setObjectName('gridLayoutUseProxyFile')

        self.useProxyFileLbl = QtWidgets.QLabel(Preferences)
        self.useProxyFileLbl.setMinimumSize(PreferenceLblMinSize)
        self.useProxyFileLbl.setObjectName('useProxyFileLbl')
        self.gridLayoutUseProxyFile.addWidget(self.useProxyFileLbl, 0, 0, 1, 1)

        self.useProxyFile = QtWidgets.QLineEdit(Preferences)
        self.useProxyFile.setMinimumSize(PreferenceSpinBoxMinSize)
        self.useProxyFile.setObjectName('useProxyFile')
        self.gridLayoutUseProxyFile.addWidget(self.useProxyFile, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayoutUseProxyFile)

        ## Using Proxyfile - checkboxes
        self.gridLayoutUseProxyFile2 = QtWidgets.QGridLayout()
        self.gridLayoutUseProxyFile2.setObjectName('gridLayoutUseProxyFile2')

        self.useProxyFileCheckBox = QtWidgets.QCheckBox("Use proxy file")
        self.useProxyFileCheckBox.setMinimumSize(PreferenceLblMinSize)
        self.useProxyFileCheckBox.setObjectName('useProxyFileCheckBox')
        self.gridLayoutUseProxyFile2.addWidget(self.useProxyFileCheckBox, 0, 0, 1, 1)

        self.checkProxyFileCheckBox = QtWidgets.QCheckBox("Check proxy file")
        self.checkProxyFileCheckBox.setMinimumSize(PreferenceLblMinSize)
        self.checkProxyFileCheckBox.setObjectName('checkProxyFileCheckBox')
        self.gridLayoutUseProxyFile2.addWidget(self.checkProxyFileCheckBox, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayoutUseProxyFile2)

        ## Buttons
        self.buttonGridLayout4 = QtWidgets.QGridLayout()
        self.buttonGridLayout4.setObjectName("buttonGridLayout4")
        self.cancelbtn = QtWidgets.QPushButton(Preferences)
        self.cancelbtn.setMinimumSize(QtCore.QSize(80, 0))
        self.cancelbtn.setObjectName("cancelbtn")
        self.cancelbtn.setStyleSheet(RedButtonStyleSheet)
        self.buttonGridLayout4.addWidget(self.cancelbtn, 0, 0, 1, 1)
        self.addbtn = QtWidgets.QPushButton(Preferences)
        self.addbtn.setMinimumSize(QtCore.QSize(80, 0))
        self.addbtn.setObjectName("addbtn")
        self.addbtn.setStyleSheet(GreenButtonStyleSheet)
        self.buttonGridLayout4.addWidget(self.addbtn, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.buttonGridLayout4)

        self.retranslateUi(Preferences)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
    
    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.inTitle1.setText(_translate("Preferences", "Preferences :"))
        self.nProxyThreadsLbl.setText(_translate("Preferences", "Number of Threads in ProxyCheck"))
        self.useProxyFileLbl.setText(_translate("Preferences", "Use a file containing proxies"))
        self.nProxyLbl.setText(_translate("Preferences", "Number of Proxies"))
        self.nThreadsLbl.setText(_translate("Preferences", "Number of Threads"))
        self.cancelbtn.setText(_translate("Preferences", "CANCEL"))
        self.addbtn.setText(_translate("Preferences", "SAVE CHANGES"))
    
    def getParameters(self):
        out = []
        out.append(self.nProxyThreads.value())
        out.append(self.nProxy.value())
        out.append(self.nThreads.value())
        out.append(self.useProxyFile.text())
        out.append(self.useProxyFileCheckBox.isChecked())
        out.append(self.checkProxyFileCheckBox.isChecked())
        return out
    
    def setParameters(self, nProxyThreads, nProxyVal, nThreadsval, proxyFilePath, useProxyFileChk, checkProxyFileChk):
        self.nProxyThreads.setValue(nProxyThreads)
        self.nProxy.setValue(nProxyVal)
        self.nThreads.setValue(nThreadsval)
        self.useProxyFile.setText(proxyFilePath)
        self.useProxyFileCheckBox.setChecked(useProxyFileChk)
        self.checkProxyFileCheckBox.setChecked(checkProxyFileChk)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        global SCREEN_HEIGHT
        global SCREEN_WIDTH
        SCREEN_HEIGHT = int(sizeObject.height())
        SCREEN_WIDTH = int(sizeObject.width())
        MainWindow.resize(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.move((SCREEN_WIDTH / 2) - (self.frameSize().width() / 2),
            (SCREEN_HEIGHT / 2) - (self.frameSize().height() / 2))
        MainWindow.setStyleSheet("background-color: rgb(28, 39, 40);\n"
"color: rgb(231, 231, 231);")
        MainWindow.setWindowIcon(QtGui.QIcon('ressources/logo.ico'))
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
        self.inputBtn.setText(_translate("MainWindow", "Choose Input File"))
        self.statBtn.setText(_translate("MainWindow", "Choose Statistics File"))
        self.outputBtn.setText(_translate("MainWindow", "Choose Output File"))
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
