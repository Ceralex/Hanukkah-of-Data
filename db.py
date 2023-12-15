import sqlite3
from sqlite3 import Error
 
def create_cursor(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    c = conn.cursor()

    return c
