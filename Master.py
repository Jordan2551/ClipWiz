import DB, pyperclip
from KM import KM
from gui import GUI
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

class Master:
    def __init__(self):
        #Call keyboard manager
        self.km = KM(self)
        #Call GUI & set it up
        self.gui = GUI(self)
        self.gui.setup()

    def copy(self, content):
        pyperclip.copy(content)

    def getData(self):
        return DB.data

    def insert_clip(self, content):
        inserted = DB.insert_clip(content)
        if inserted:
            self.gui.ins_data_in_table(inserted, False)

    def search(self, text):
        return DB.search(text)


m = Master()
