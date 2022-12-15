# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphicCMS.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

dialog_style_sheet = "background-color: rgb(45, 45, 45);\n""color: rgb(211, 211, 211);\n""font: 11pt \"Ubuntu Mono\";" \
                     "font-weight: bold"
table_view_style_sheet = "background-color: rgb(70, 70, 70);\n"
green_button_style_sheet = "background-color: rgb(71, 141, 75);\n""color: rgb(45, 45, 45);\n" \
                           "border-color: rgb(0, 80, 0);"
red_button_style_sheet = "background-color: rgb(170, 16, 16);\n""color: rgb(45, 45, 45);\n" \
                         "border-color: rgb(80, 0, 0);"
blue_button_style_sheet = "background-color: rgb(77, 84, 176);\n""color: rgb(45, 45, 45);\n" \
                          "border-color: rgb(0, 0, 80);"

_MAXVALUE_ = 999999999
SCREEN_HEIGHT = 0
SCREEN_WIDTH = 0

preference_lbl_min_size = QtCore.QSize(int(SCREEN_WIDTH / 5.8), 20)
preference_spinbox_min_size = QtCore.QSize(int(SCREEN_WIDTH / 5.8), 20)


class UIpreferences(object):
    def __init__(self):
        self.add_btn = None
        self.button_gridlayout_4 = None
        self.cancel_btn = None
        self.check_proxy_file_check_box = None
        self.grid_layout_3 = None
        self.grid_layout_t_i = None
        self.grid_layout_proxy_check = None
        self.grid_layout_proxy_needed = None
        self.grid_layout_use_proxy_file = None
        self.grid_layout_use_proxy_file_2 = None
        self.in_title_1 = None
        self.n_threads = None
        self.n_threads_lbl = None
        self.n_proxy = None
        self.n_proxy_lbl = None
        self.n_proxy_threads = None
        self.n_proxy_threads_lbl = None
        self.use_proxy_file = None
        self.use_proxy_file_check_box = None
        self.use_proxy_file_lbl = None
        self.vertical_layout = None

    def setup_ui(self, preferences):
        preferences.setObjectName("preferences")
        preferences.resize(int(SCREEN_WIDTH / 2.7), int(SCREEN_HEIGHT / 4.8))
        preferences.setFixedSize(int(SCREEN_WIDTH / 2.7), int(SCREEN_HEIGHT / 3.5))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        preferences.setSizePolicy(sizePolicy)

        self.vertical_layout = QtWidgets.QVBoxLayout(preferences)
        self.vertical_layout.setObjectName("vertical_layout")

        # Title
        self.grid_layout_t_i = QtWidgets.QGridLayout()
        self.grid_layout_t_i.setObjectName('grid_layout_t_i')
        self.in_title_1 = QtWidgets.QLabel(preferences)
        self.in_title_1.setMinimumSize(preference_lbl_min_size)
        self.in_title_1.setBaseSize(preference_lbl_min_size)
        self.in_title_1.setObjectName("in_title_1")
        self.grid_layout_t_i.addWidget(self.in_title_1, 0, 0, 1, 1)
        self.vertical_layout.addLayout(self.grid_layout_t_i)

        # Number of Threads in scraping
        self.grid_layout_3 = QtWidgets.QGridLayout()
        self.grid_layout_3.setObjectName('grid_layout_3')
        self.n_threads_lbl = QtWidgets.QLabel(preferences)
        self.n_threads_lbl.setMinimumSize(preference_lbl_min_size)
        self.n_threads_lbl.setObjectName('n_threads_lbl')
        self.grid_layout_3.addWidget(self.n_threads_lbl, 0, 0, 1, 1)
        self.n_threads = QtWidgets.QSpinBox(preferences)
        self.n_threads.setMinimumSize(preference_spinbox_min_size)
        self.n_threads.setBaseSize(preference_spinbox_min_size)
        self.n_threads.setObjectName('n_threads')
        self.n_threads.setMaximum(_MAXVALUE_)
        self.grid_layout_3.addWidget(self.n_threads, 0, 1, 1, 1)
        self.vertical_layout.addLayout(self.grid_layout_3)

        # Number of Threads in proxyChecking
        self.grid_layout_proxy_check = QtWidgets.QGridLayout()
        self.grid_layout_proxy_check.setObjectName('grid_layout_proxy_check')

        self.n_proxy_threads_lbl = QtWidgets.QLabel(preferences)
        self.n_proxy_threads_lbl.setMinimumSize(preference_lbl_min_size)
        self.n_proxy_threads_lbl.setObjectName('n_proxy_threads_lbl')
        self.grid_layout_proxy_check.addWidget(self.n_proxy_threads_lbl, 0, 0, 1, 1)

        self.n_proxy_threads = QtWidgets.QSpinBox(preferences)
        self.n_proxy_threads.setMinimumSize(preference_spinbox_min_size)
        self.n_proxy_threads.setBaseSize(preference_spinbox_min_size)
        self.n_proxy_threads.setObjectName('n_proxy_threads')
        self.grid_layout_proxy_check.addWidget(self.n_proxy_threads, 0, 1, 1, 1)
        self.vertical_layout.addLayout(self.grid_layout_proxy_check)

        # Number of Proxies needed
        self.grid_layout_proxy_needed = QtWidgets.QGridLayout()
        self.grid_layout_proxy_needed.setObjectName('grid_layout_proxy_needed')

        self.n_proxy_lbl = QtWidgets.QLabel(preferences)
        self.n_proxy_lbl.setMinimumSize(preference_lbl_min_size)
        self.n_proxy_lbl.setObjectName('n_proxy_lbl')
        self.grid_layout_proxy_needed.addWidget(self.n_proxy_lbl, 0, 0, 1, 1)

        self.n_proxy = QtWidgets.QSpinBox(preferences)
        self.n_proxy.setMinimumSize(preference_spinbox_min_size)
        self.n_proxy.setBaseSize(preference_spinbox_min_size)
        self.n_proxy.setObjectName('n_proxy')
        self.grid_layout_proxy_needed.addWidget(self.n_proxy, 0, 1, 1, 1)
        self.vertical_layout.addLayout(self.grid_layout_proxy_needed)

        # Using a proxy_file
        self.grid_layout_use_proxy_file = QtWidgets.QGridLayout()
        self.grid_layout_use_proxy_file.setObjectName('grid_layout_use_proxy_file')

        self.use_proxy_file_lbl = QtWidgets.QLabel(preferences)
        self.use_proxy_file_lbl.setMinimumSize(preference_lbl_min_size)
        self.use_proxy_file_lbl.setObjectName('use_proxy_file_lbl')
        self.grid_layout_use_proxy_file.addWidget(self.use_proxy_file_lbl, 0, 0, 1, 1)

        self.use_proxy_file = QtWidgets.QLineEdit(preferences)
        self.use_proxy_file.setMinimumSize(preference_spinbox_min_size)
        self.use_proxy_file.setObjectName('use_proxy_file')
        self.grid_layout_use_proxy_file.addWidget(self.use_proxy_file, 0, 1, 1, 1)
        self.vertical_layout.addLayout(self.grid_layout_use_proxy_file)

        # Using Proxyfile - checkboxes
        self.grid_layout_use_proxy_file_2 = QtWidgets.QGridLayout()
        self.grid_layout_use_proxy_file_2.setObjectName('grid_layout_use_proxy_file_2')

        self.use_proxy_file_check_box = QtWidgets.QCheckBox("Use proxy file")
        self.use_proxy_file_check_box.setMinimumSize(preference_lbl_min_size)
        self.use_proxy_file_check_box.setObjectName('use_proxy_file_check_box')
        self.grid_layout_use_proxy_file_2.addWidget(self.use_proxy_file_check_box, 0, 0, 1, 1)

        self.check_proxy_file_check_box = QtWidgets.QCheckBox("Check proxy file")
        self.check_proxy_file_check_box.setMinimumSize(preference_lbl_min_size)
        self.check_proxy_file_check_box.setObjectName('check_proxy_file_check_box')
        self.grid_layout_use_proxy_file_2.addWidget(self.check_proxy_file_check_box, 0, 1, 1, 1)

        self.vertical_layout.addLayout(self.grid_layout_use_proxy_file_2)

        # Buttons
        self.button_gridlayout_4 = QtWidgets.QGridLayout()
        self.button_gridlayout_4.setObjectName("button_gridlayout_4")
        self.cancel_btn = QtWidgets.QPushButton(preferences)
        self.cancel_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.setStyleSheet(red_button_style_sheet)
        self.button_gridlayout_4.addWidget(self.cancel_btn, 0, 0, 1, 1)
        self.add_btn = QtWidgets.QPushButton(preferences)
        self.add_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.add_btn.setObjectName("add_btn")
        self.add_btn.setStyleSheet(green_button_style_sheet)
        self.button_gridlayout_4.addWidget(self.add_btn, 0, 1, 1, 1)
        self.vertical_layout.addLayout(self.button_gridlayout_4)

        self.retranslate_ui(preferences)
        QtCore.QMetaObject.connectSlotsByName(preferences)

    def retranslate_ui(self, preferences):
        _translate = QtCore.QCoreApplication.translate
        preferences.setWindowTitle(_translate("preferences", "preferences"))
        self.in_title_1.setText(_translate("preferences", "preferences :"))
        self.n_proxy_threads_lbl.setText(_translate("preferences", "Number of Threads in ProxyCheck"))
        self.use_proxy_file_lbl.setText(_translate("preferences", "Use a file containing proxies"))
        self.n_proxy_lbl.setText(_translate("preferences", "Number of Proxies"))
        self.n_threads_lbl.setText(_translate("preferences", "Number of Threads"))
        self.cancel_btn.setText(_translate("preferences", "CANCEL"))
        self.add_btn.setText(_translate("preferences", "SAVE CHANGES"))

    def getParameters(self):
        out = [self.n_proxy_threads.value(), self.n_proxy.value(), self.n_threads.value(), self.use_proxy_file.text(),
               self.use_proxy_file_check_box.isChecked(), self.check_proxy_file_check_box.isChecked()]
        return out

    def setParameters(self, n_proxy_threads, n_proxy_val, n_threads_val, proxy_file_path, use_proxy_file_chk,
                      check_proxy_file_chk):
        self.n_proxy_threads.setValue(n_proxy_threads)
        self.n_proxy.setValue(n_proxy_val)
        self.n_threads.setValue(n_threads_val)
        self.use_proxy_file.setText(proxy_file_path)
        self.use_proxy_file_check_box.setChecked(use_proxy_file_chk)
        self.check_proxy_file_check_box.setChecked(check_proxy_file_chk)


class UiMainWindow(object):
    def __init__(self):
        self.action_hello = None
        self.console_lbl = None
        self.console_disp = None
        self.console_layout = None
        self.progress_bar = None
        self.chosen_out_lbl = None
        self.chosen_stat_lbl = None
        self.chosen_file_lbl = None
        self.vertical_layout_2 = None
        self.run_btn = None
        self.output_btn = None
        self.stat_btn = None
        self.vertical_layout = None
        self.horizontal_layout = None
        self.proxy_btn = None
        self.vertical_layout_prox = None
        self.grid_layout = None
        self.central_widget = None
        self.input_btn = None

    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        global SCREEN_HEIGHT
        global SCREEN_WIDTH
        SCREEN_HEIGHT = int(sizeObject.height())
        SCREEN_WIDTH = int(sizeObject.width())
        main_window.resize(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.move((SCREEN_WIDTH / 2) - (self.frameSize().width() / 2),
                  (SCREEN_HEIGHT / 2) - (self.frameSize().height() / 2))
        main_window.setStyleSheet("background-color: rgb(28, 39, 40);\n"
                                  "color: rgb(231, 231, 231);")
        main_window.setWindowIcon(QtGui.QIcon('ressources/logo.ico'))
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        # Grid Layout containing everything
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("grid_layout")

        # Vertical Layout for 
        # proxies ?
        # < buttons | labels >
        self.vertical_layout_prox = QtWidgets.QVBoxLayout()
        self.vertical_layout_prox.setObjectName("vertical_layout_prox")

        # ## Switch at the top for Proxies or Proxyless
        self.proxy_btn = QtWidgets.QPushButton(self.central_widget)
        self.proxy_btn.setMinimumSize(QtCore.QSize(131, 23))
        self.proxy_btn.setObjectName("proxy_btn")
        self.vertical_layout_prox.addWidget(self.proxy_btn)
        # ## ------------

        # Horizontal Layout for < buttons | labels >
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        # Vertical Layout for the buttons
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")

        # input button
        self.input_btn = QtWidgets.QPushButton(self.central_widget)
        self.input_btn.setMinimumSize(QtCore.QSize(131, 23))
        self.input_btn.setObjectName("input_btn")
        self.vertical_layout.addWidget(self.input_btn)
        # stat button
        self.stat_btn = QtWidgets.QPushButton(self.central_widget)
        self.stat_btn.setMinimumSize(QtCore.QSize(131, 23))
        self.stat_btn.setObjectName("stat_btn")
        self.vertical_layout.addWidget(self.stat_btn)
        # output button
        self.output_btn = QtWidgets.QPushButton(self.central_widget)
        self.output_btn.setMinimumSize(QtCore.QSize(131, 23))
        self.output_btn.setObjectName("output_btn")
        self.vertical_layout.addWidget(self.output_btn)
        # run button
        self.run_btn = QtWidgets.QPushButton(self.central_widget)
        self.run_btn.setMinimumSize(QtCore.QSize(131, 23))
        self.run_btn.setObjectName("run_btn")
        self.vertical_layout.addWidget(self.run_btn)

        self.horizontal_layout.addLayout(self.vertical_layout)
        self.vertical_layout_prox.addLayout(self.horizontal_layout)

        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        # input Label
        self.chosen_file_lbl = QtWidgets.QLabel(self.central_widget)
        self.chosen_file_lbl.setMinimumSize(QtCore.QSize(200, 23))
        self.chosen_file_lbl.setStyleSheet("color: rgb(156, 156, 156);\n"
                                         "background-color: rgb(61, 61, 61);\n"
                                         "border-color: rgb(71, 71, 71);")
        self.chosen_file_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.chosen_file_lbl.setObjectName("chosen_file_lbl")
        self.vertical_layout_2.addWidget(self.chosen_file_lbl)
        # stat Label
        self.chosen_stat_lbl = QtWidgets.QLabel(self.central_widget)
        self.chosen_stat_lbl.setMinimumSize(QtCore.QSize(200, 23))
        self.chosen_stat_lbl.setStyleSheet("color: rgb(156, 156, 156);\n"
                                         "background-color: rgb(61, 61, 61);\n"
                                         "border-color: rgb(71, 71, 71);")
        self.chosen_stat_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.chosen_stat_lbl.setObjectName("chosen_stat_lbl")
        self.vertical_layout_2.addWidget(self.chosen_stat_lbl)
        # output label
        self.chosen_out_lbl = QtWidgets.QLabel(self.central_widget)
        self.chosen_out_lbl.setMinimumSize(QtCore.QSize(200, 23))
        self.chosen_out_lbl.setStyleSheet("color: rgb(156, 156, 156);\n"
                                        "background-color: rgb(61, 61, 61);\n"
                                        "border-color: rgb(71, 71, 71);\n"
                                        "")
        self.chosen_out_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.chosen_out_lbl.setObjectName("chosen_out_lbl")
        self.vertical_layout_2.addWidget(self.chosen_out_lbl)
        # Progress bar
        self.progress_bar = QtWidgets.QProgressBar(self.central_widget)
        self.progress_bar.setMinimumSize(QtCore.QSize(200, 23))
        self.progress_bar.setStyleSheet("QProgressBar{\n"
                                       "    border: 2px solid rgb(139, 28, 59);\n"
                                       "    border-radius: 5px;\n"
                                       "    text-align: center\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: rgb(172, 35, 72);\n"
                                       "    width: 10px;\n"
                                       "}")
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setObjectName("progress_bar")
        self.vertical_layout_2.addWidget(self.progress_bar)
        self.horizontal_layout.addLayout(self.vertical_layout_2)
        self.grid_layout.addLayout(self.vertical_layout_prox, 0, 0, 1, 1)
        # Console Display
        self.console_layout = QtWidgets.QVBoxLayout()
        self.console_layout.setObjectName("console_layout")
        self.console_lbl = QtWidgets.QLabel(self.central_widget)
        self.console_lbl.setMinimumSize(QtCore.QSize(101, 16))
        self.console_lbl.setStyleSheet("background-color: rgb(47, 66, 68);\n"
                                      "color: rgb(231, 231, 231);\n"
                                      "border-color: rgb(47, 47, 47);")
        self.console_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.console_lbl.setObjectName("console_lbl")
        self.console_layout.addWidget(self.console_lbl)
        self.console_disp = QtWidgets.QTextEdit(self.central_widget)
        self.console_disp.setMinimumSize(QtCore.QSize(339, 113))
        self.console_disp.setSizeIncrement(QtCore.QSize(3, 1))
        self.console_disp.setStyleSheet("color: rgb(38, 209, 0);\n"
                                       "border-color: rgb(71, 71, 71);\n"
                                       "background-color: rgb(0, 0, 0);")
        self.console_disp.setReadOnly(True)
        self.console_disp.setObjectName("console_disp")
        self.console_layout.addWidget(self.console_disp)
        self.grid_layout.addLayout(self.console_layout, 1, 0, 1, 1)
        main_window.setCentralWidget(self.central_widget)
        self.action_hello = QtWidgets.QAction(main_window)
        self.action_hello.setObjectName("action_hello")

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "CMScrape - CardMarket Price Tracker"))
        self.proxy_btn.setText(_translate("main_window", "Without Proxies (limited to 30/min)"))
        self.input_btn.setText(_translate("main_window", "Choose Input File"))
        self.stat_btn.setText(_translate("main_window", "Choose Statistics File"))
        self.output_btn.setText(_translate("main_window", "Choose Output File"))
        self.run_btn.setText(_translate("main_window", "Run"))
        self.chosen_file_lbl.setText(_translate("main_window", "No file chosen"))
        self.chosen_stat_lbl.setText(_translate("main_window", "No file chosen"))
        self.chosen_out_lbl.setText(_translate("main_window", "No file chosen"))
        self.action_hello.setText(_translate("main_window", "Hello"))
        self.console_lbl.setText(_translate("main_window", "Console output :"))  #


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    # ## What should be done is putting only the \r'd text in the console, rewriting it, and append the errors I could
    # ## in the begining or end of string, to be shown if user wants to.
    # ## maybe yet another argument "-se, --show-errors" that would work in cmd and
    MainWindow.show()
    sys.exit(app.exec_())
