import sqlite3
from datetime import datetime

class DB:

    def __init__(self):
        with sqlite3.connect('database.db', check_same_thread=False) as self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('CREATE TABLE IF NOT EXISTS Clips (id INTEGER PRIMARY KEY, content TEXT, clipStamp TEXT)')
            self.conn.commit()
            #Initialize data list with all content
            self.data = self.select_all()

    def select_all(self):
        return self.cursor.execute("SELECT * FROM Clips").fetchall()

    def insert_clip(self, content):
        if content != '':
            try:
                self.cursor.execute("INSERT INTO CLIPS (content, clipStamp) VALUES(?,?)", (content, datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                self.conn.commit()
                inserted = self.cursor.execute("SELECT * FROM Clips ORDER BY ID DESC LIMIT 1").fetchone()
                print(type(inserted))
                self.data.append(inserted)
                return [inserted] #Must return as list of tuples!
            except sqlite3.Error as e:
                print(e)
                return False

    def search(self, text):
        try:
            return self.cursor.execute("SELECT * FROM Clips WHERE content LIKE ?",('%'+text+'%',)).fetchall()
        except sqlite3.Error as e:
            print(e)

    def reset(self):
        try:
            self.cursor.execute('DELETE FROM Clips')
            self.conn.commit()
            self.data = self.select_all() #SCOPING ISSUE!
        except sqlite3.Error as e:
            print(e)