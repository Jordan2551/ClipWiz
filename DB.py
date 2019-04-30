import sqlite3
from datetime import datetime

with sqlite3.connect('database.db', check_same_thread=False) as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Clips (id INTEGER PRIMARY KEY, content TEXT, clipStamp TEXT)')
    conn.commit()

def select_all():
    return cursor.execute("SELECT * FROM Clips").fetchall()

#Initialize data list with all content
data = select_all()


def insert_clip(content):
    if content != '':
        try:
            cursor.execute("INSERT INTO CLIPS (content, clipStamp) VALUES(?,?)", (content, datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
            conn.commit()
            inserted = cursor.execute("SELECT * FROM Clips ORDER BY ID DESC LIMIT 1").fetchone()
            print(type(inserted))
            data.append(inserted)
            return [inserted] #Must return as list of tuples!
        except sqlite3.Error as e:
            print(e)
            return False

def search(text):
    try:
        return cursor.execute("SELECT * FROM Clips WHERE content LIKE ?",('%'+text+'%',)).fetchall()
    except sqlite3.Error as e:
        print(e)

def reset():
    try:
        cursor.execute('DELETE FROM Clips')
        conn.commit()
        data = select_all() #SCOPING ISSUE!
    except sqlite3.Error as e:
        print(e)