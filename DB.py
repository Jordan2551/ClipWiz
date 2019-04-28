import sqlite3
import enum
from datetime import datetime

class DB:

    db_file = 'database.db'

    def __init__(self):
        self.conn = sqlite3.connect(DB.db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Clips (id INTEGER PRIMARY KEY, content TEXT, clipStamp TEXT)')

    def select_all(self):
        return self.cursor.execute("SELECT * FROM Clips").fetchall()

    def insert_clip(self, content):
        self.cursor.execute("INSERT INTO CLIPS (content, clipStamp) VALUES(?,?)", (content, datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        self.conn.commit()

    def insert_dummy(self):
        self.cursor.execute("INSERT INTO Clips (content, clipStamp) VALUES(?, ?)",("Hi this test", "2013-03-06 10:10:10"))
        self.cursor.execute("INSERT INTO Clips (content, clipStamp) VALUES(?, ?)",("Hi this test3", "2018-03-06 10:10:10"))
        self.conn.commit()

    def search(self, text):
        return self.cursor.execute("SELECT * FROM Clips WHERE content LIKE ?",('%'+text+'%',)).fetchall()

    def print_cursor(self):
        #Using the ? palceholder to avoid SQL injection
        self.cursor.execute("SELECT * FROM Clips WHERE content=?",("Hi this test3",))
        all_rows = self.cursor.fetchall()

