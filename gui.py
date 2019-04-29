# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication, QClipboard
from KM import KM
import pyperclip
import DB

class Ui_MainWindow(object):

    def set_data_table(self):
        header = self.dataTable.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.dataTable.cellClicked.connect(self.row_copy)
        print(DB.data)
        for rowi, row in enumerate(DB.data):
                self.dataTable.insertRow(rowi)
                for coli, col in enumerate(row):
                        self.dataTable.setItem(rowi, coli, QtWidgets.QTableWidgetItem(str(col)))

    def row_copy(self, row, col):
        #Get the clip content from the corresponding cell into clipboard
        pyperclip.copy(self.dataTable.item(row, 1).text())


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 772)
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
        self.label.setGeometry(QtCore.QRect(60, 20, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.searchContent = QtWidgets.QLineEdit(self.centralwidget)
        self.searchContent.setGeometry(QtCore.QRect(130, 70, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.searchContent.setFont(font)
        self.searchContent.setText("")
        self.searchContent.setObjectName("searchContent")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 81, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(600, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.resetBtn.setFont(font)
        self.resetBtn.setStyleSheet("")
        self.resetBtn.setObjectName("resetBtn")
        self.changeKBBtn = QtWidgets.QPushButton(self.centralwidget)
        self.changeKBBtn.setGeometry(QtCore.QRect(410, 610, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.changeKBBtn.setFont(font)
        self.changeKBBtn.setStyleSheet("")
        self.changeKBBtn.setObjectName("changeKBBtn")
        self.setKB = QtWidgets.QLineEdit(self.centralwidget)
        self.setKB.setGeometry(QtCore.QRect(180, 610, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.setKB.setFont(font)
        self.setKB.setStyleSheet("")
        self.setKB.setText("")
        self.setKB.setObjectName("setKB")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 570, 231, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(180, 550, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(60, 50, 641, 20))
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
        self.label_5.setGeometry(QtCore.QRect(70, 480, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.dataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dataTable.setGeometry(QtCore.QRect(60, 120, 641, 361))
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(3)
        self.dataTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.dataTable.setHorizontalHeaderItem(2, item)
        self.set_data_table()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Clip Board History"))
        self.searchContent.setPlaceholderText(_translate("MainWindow", "Search for clip.."))
        self.label_2.setText(_translate("MainWindow", "Search"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.changeKBBtn.setText(_translate("MainWindow", "Change"))
        self.label_3.setText(_translate("MainWindow", "Clip Cycle Keybind"))
        self.label_4.setText(_translate("MainWindow", "Options"))
        self.label_5.setText(_translate("MainWindow", "• Pro tip: click table row to copy contents to clipboard "))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id   "))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Content"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timestamp    "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #Call keyboard manager
    km = KM()
    sys.exit(app.exec_())

