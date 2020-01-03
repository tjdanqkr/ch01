import sqlite3
from sqlite3 import Error




class c:

    def __init__(self, name):
        self.name = name

    def tc(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        conn = sqlite3.connect("test1.db")
        conn.execute("CREATE TABLE " + self.name + "('" + self.val1 + "','" + self.val2 + "')")
        conn.commit()
        conn.close()

    def ti(self, vali1, vali2):
        self.vali1 = vali1
        self.vali2 = vali2
        conn = sqlite3.connect("test1.db")
        conn.execute(
            "insert into " + self.name + "('" + self.val1 + "','" + self.val2 + "')" + "values('" + self.vali1 + "','" + self.vali2 + "')")
        conn.commit()
        conn.close()

    def ts(self):
        conn = sqlite3.connect("test1.db")
        cursor = conn.execute("select *from "+self.name)
        for book in cursor.fetchall():
            print(book)
        conn.close()

    def tso(self, text):
        self.text = text
        conn = sqlite3.connect("test1.db")
        cursor = conn.execute("select *from "+self.name)
        f= open(self.text,"w", encoding='utf-8')
        for book in cursor.fetchall():
            f.write(str(book)+"\n")
        f.close()
        conn.close()

    def tsr(self):
        f = open(self.text, "r")
        print(f.read())
        f.close()