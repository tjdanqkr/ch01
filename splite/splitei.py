import sqlite3
from sqlite3 import Error
class i :
    def __init__(self):
        conn = sqlite3.connect("test.db")

        conn.close()