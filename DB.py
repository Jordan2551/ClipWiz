import sqlite3
from datetime import datetime

db_file = 'database.db'

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Clips (id INTEGER PRIMARY KEY, content TEXT, clipStamp TEXT)')


def select_all():
    return cursor.execute("SELECT * FROM Clips").fetchall()

#Initialize data list with all content
data = select_all()

def insert_clip(content):
    try:
        cursor.execute("INSERT INTO CLIPS (content, clipStamp) VALUES(?,?)", (content, datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        data.add(content)
    except sqlite3.Error as e:
        print(e.__cause__)

def insert_dummy():
    cursor.execute("INSERT INTO Clips (content, clipStamp) VALUES(?, ?)",("Hi this test", "2013-03-06 10:10:10"))
    cursor.execute("INSERT INTO Clips (content, clipStamp) VALUES(?, ?)",("Hi this test3", "2018-03-06 10:10:10"))
    conn.commit()

def search(text):
    try:
        return cursor.execute("SELECT * FROM Clips WHERE content LIKE ?",('%'+text+'%',)).fetchall()
    except sqlite3.Error as e:
        print(e.__cause__)

def print_cursor():
    #Using the ? palceholder to avoid SQL injection
    cursor.execute("SELECT * FROM Clips WHERE content=?",("Hi this test3",))
    all_rows = cursor.fetchall()

