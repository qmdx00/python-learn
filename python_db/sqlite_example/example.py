import os
import sqlite3

"""
create db file
"""
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

"""
init db connect and cursor
"""
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("create table user (id varchar(20) primary key , name varchar(20))")
cursor.execute("insert into user(id, name ) values('001', 'Alice')")

cursor.close()
conn.commit()
conn.close()


conn = sqlite3.connect(db_file)
cur = conn.cursor()
cur.execute("select * from user")
print(cur.fetchall())
cur.close()
conn.close()
