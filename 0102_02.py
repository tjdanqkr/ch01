# 파이선 데이타 베이스

import sqlite3
from sqlite3 import Error
# spllite 3 버전 다운
# sudo apt-get install sqlite3
# conn = sqlite3.connect("test.db")
# #
# # # conn.execute("CREATE TABLE book( no integer primary key autoincrement , title text not null, price integer)")
# # # conn.execute("insert into book(no,title,price) values(4,'c++',20000)")
# # #
# # # conn.execute("insert into book(no,title,price) values(5,'python',30000)")
# #
# # conn.commit()
# # cursor = conn.execute("select *from book")
# # for book in cursor.fetchall() :
# #     print(book)
# #
# # conn.close()


from peewee import *

db = SqliteDatabase('peewee1.db')


class Book(Model):
    no = IntegerField(primary_key=True)
    title = CharField()
    price = IntegerField()

    class Meta:
        database = db


db.connect()
db.create_tables([Book])
b1 = Book.create(no=1, title='python', price=20000)
b1.save()
b1 = Book.create(no=2, title='C#', price=40000)
b1.save()

for book in Book.select():
    print('%5d %10s %8d' % (book.no, book.title, book.price))

db.close()
