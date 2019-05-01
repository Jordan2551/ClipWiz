import pyperclip
from DB import DB
from KM import KM
from GUI import Ui_MainWindow
import sys

class Master:
    def __init__(self):
        #Set up DB
        self.db = DB()
        #Call keyboard manager
        self.km = KM(self)
        #Call GUI & set it up
        self.gui = Ui_MainWindow(self)
        self.gui.setup()

    def copy(self, content):
        pyperclip.copy(content)

    def getData(self):
        return self.db.data

    def insert_clip(self, content):
        inserted = self.db.insert_clip(content)
        if inserted:
            self.gui.ins_data_in_table(inserted, False)

    def search(self, text):
        return self.db.search(text)

    def reset(self):
        self.db.reset()


m = Master()
