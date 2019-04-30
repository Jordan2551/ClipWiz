# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):

    def __init__(self, master):
        self.master = master

    def setup(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    def set_data_table(self):
        header = self.dataTable.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.dataTable.cellClicked.connect(self.row_copy)
        self.ins_data_in_table(self.master.getData())
        self.dataTable.verticalHeader().hide()

    #Get the clip content from the corresponding cell into clipboard
    def row_copy(self, row):
        self.master.copy(self.dataTable.item(row, 1).text())

    #Inserts data into table from a list.
    #resetdata - true if the entire table should be wiped (used for setup and search functionality) false used by new clipboard inserts
    def ins_data_in_table(self, data, resetData=True):
        if resetData:
                self.dataTable.setRowCount(0)
        for rowi, row in enumerate(data):
                #When just inserting a new clip we want to insert at LAST index in table!
                if resetData == False:
                        rowi = self.dataTable.rowCount()
                self.dataTable.insertRow(rowi)
                for coli, col in enumerate(row):
                        self.dataTable.setItem(rowi, coli, QtWidgets.QTableWidgetItem(str(col)))

    def reset_db(self):
        self.master.reset()
        self.dataTable.setRowCount(0)

    def reset_content(self):
        self.searchContent.setText("")
        self.ins_data_in_table(self.master.getData())

    def search(self):
        if self.searchContent.text() == "":
            self.ins_data_in_table(self.master.getData())
        else:
            self.ins_data_in_table(self.master.search(self.searchContent.text()))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 770)
        MainWindow.setMinimumSize(QtCore.QSize(830, 770))
        MainWindow.setMaximumSize(QtCore.QSize(830, 770))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rsc/rsc/wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"    background-image:url(\'C:/Users/falador/Google Drive/Wallpapers/dark_polygon01.png\');\n"
"}\n"
"\n"
"QLabel{\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: #0288D1;\n"
"    border-style: solid;\n"
"    border-color: #0288D1;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
" QPushButton:hover {\n"
"     background-color: #0288D1;\n"
"     border-color: white;\n"
"     color: white;\n"
" }\n"
"\n"
" QLineEdit{\n"
"    border-radius: 10px;\n"
"    color: #0288D1;\n"
"    padding: 2px;\n"
"    height: 75px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.searchContent = QtWidgets.QLineEdit(self.centralwidget)
        self.searchContent.setGeometry(QtCore.QRect(170, 60, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.searchContent.setFont(font)
        self.searchContent.setText("")
        self.searchContent.setObjectName("searchContent")
        self.searchContent.textChanged.connect(self.search)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 81, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(640, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.resetBtn.setFont(font)
        self.resetBtn.setStyleSheet("")
        self.resetBtn.setObjectName("resetBtn")
        self.resetBtn.clicked.connect(self.reset_content)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(100, 40, 641, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 570, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.dataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dataTable.setGeometry(QtCore.QRect(90, 110, 651, 361))
        self.dataTable.setMouseTracking(True)
        self.dataTable.setToolTipDuration(5)
        self.dataTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dataTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.dataTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(3)
        self.dataTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(1, 2, item)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 470, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 510, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 550, 641, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line_3.setFont(font)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 600, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 670, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 670, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/rsc/rsc/python.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(305, 670, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/rsc/rsc/heart.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(340, 670, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 670, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(420, 670, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:red")
        self.label_13.setOpenExternalLinks(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(520, 670, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(550, 670, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/rsc/rsc/Law_rune_detail.png"))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(590, 670, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/rsc/rsc/Earth_rune_detail.png"))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(630, 670, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/rsc/rsc/Air_rune_detail.png"))
        self.label_17.setObjectName("label_17")
        self.resetTblBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetTblBtn.setGeometry(QtCore.QRect(620, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.resetTblBtn.setFont(font)
        self.resetTblBtn.setStyleSheet("")
        self.resetTblBtn.setObjectName("resetTblBtn")
        self.resetTblBtn.clicked.connect(self.reset_db)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.set_data_table()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ClipWiz - JC Software"))
        self.label.setText(_translate("MainWindow", "Clip Board History"))
        self.searchContent.setPlaceholderText(_translate("MainWindow", "Search for clip.."))
        self.label_2.setText(_translate("MainWindow", "Search"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.label_5.setText(_translate("MainWindow", "• To go through your clipboard history use ctrl + alt + c twice. Press again to go back more"))
        item = self.dataTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.dataTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Content"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timestamp"))
        __sortingEnabled = self.dataTable.isSortingEnabled()
        self.dataTable.setSortingEnabled(False)
        item = self.dataTable.item(0, 0)
        item.setText(_translate("MainWindow", "12"))
        item = self.dataTable.item(0, 1)
        item.setText(_translate("MainWindow", "Hello"))
        item = self.dataTable.item(0, 2)
        item.setText(_translate("MainWindow", "12:34:5453"))
        item = self.dataTable.item(1, 0)
        item.setText(_translate("MainWindow", "13"))
        item = self.dataTable.item(1, 1)
        item.setText(_translate("MainWindow", "My name is Jordan"))
        item = self.dataTable.item(1, 2)
        item.setText(_translate("MainWindow", "43432434"))
        self.dataTable.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "• Pro tip: click table row to copy contents to clipboard "))
        self.label_3.setText(_translate("MainWindow", "Help"))
        self.label_7.setText(_translate("MainWindow", "• You can search for specific clipboard content by going to the search box above the table"))
        self.label_8.setText(_translate("MainWindow", "Developed with "))
        self.label_11.setText(_translate("MainWindow", "in"))
        self.label_12.setText(_translate("MainWindow", "by"))
        self.label_13.setText(_translate("MainWindow", "<a href=\"http://www.jcsoftware.ca\" style=\"color:#0288D1;\">JC Software</a>"))
        self.label_14.setText(_translate("MainWindow", "at"))
        self.resetTblBtn.setText(_translate("MainWindow", "Reset Table"))

import rsc_rc


